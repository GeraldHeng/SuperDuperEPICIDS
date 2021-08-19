from opcua import Client
from colorama import init, Fore, Back, Style
import numpy as np
import time
from flask import Flask, render_template, send_file
import random
import re
import sys
from turbo_flask import Turbo
import threading

import helpers.client_helper_funcs as helper
from classes.switch import Switch
from classes.ied import Ied
from classes.case import Case
from helpers.constant import *
import json
import paho.mqtt.client as mqttClient
from datetime import datetime

app = Flask(__name__)
turbo = Turbo(app)
logs = []

# Count to 79 as each subscribe interval will have 79 message.
line_counter = 0
cycle = 0
temp_variable_dict = {}
serverClient = None
# current_source = 'mqtt'
current_source = 'log'


class ServerClient:
    def __init__(self, server_ip=None, port=None, topic=None, on_connect=None, on_message=None):
        # When it is None, use for MQTT logs only.
        self.variables = {}
        if server_ip is not None:
            self.server = mqttClient.Client('client')
            self.server.on_connect = on_connect
            self.server.on_message = on_message

        self.broker_address = server_ip
        self.port = port
        self.topic = topic

    def connect(self):
        print('connecting')
        self.server.connect(self.broker_address, port=self.port)
        self.server.loop_start()
        time.sleep(1)
        self.server.subscribe(self.topic)

    def sort_by_origin(self):
        origins = {'Errors': []}
        for k, variable in self.variables.items():
            if not isinstance(variable, str):
                # For error component to be displayed.
                if not variable.consistent_status:
                    origins['Errors'].append(variable)

                if variable.origin in origins:
                    origins[variable.origin].append(variable)
                else:
                    origins[variable.origin] = [variable]

        return origins


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected to broker')
    else:
        print('Connection failed')


# When message read from server, this is where it will go. Use for dt mode.
def on_message(client, userdata, message):
    global line_counter
    global temp_variable_dict
    global serverClient
    global cycle
    dt_item = json.loads(message.payload.decode("utf-8"))[0]

    # Get the name of the component.
    name = dt_item['value'][(dt_item['value'].find(
        ']') + 1): dt_item['value'].find(':')].strip()

    # To find the component and element split point.
    c_index = len(name) - 1
    for c in name[::-1]:
        if c == '_':
            break
        c_index -= 1

    component = name[0: c_index]
    element = name[c_index + 1: len(name)]

    # Get the value of the component.
    value = float(dt_item['value'][dt_item['value'].find(
        ':')+1: len(dt_item['value'])].strip())


    line_counter += 1

    if component in temp_variable_dict:
        temp_variable_dict[component][element] = value
    else:
        temp_variable_dict[component] = {element: value}

    if line_counter >= 79:
        line_counter = 0
        cycle += 1
        for component, component_val in DT_VALUES.items():
            for item, item_val in component_val.items():
                if item_val['type'] is 'switch':
                    Switch.define_switch_dt(
                        item, temp_variable_dict[item], serverClient.variables, component)
                elif item_val['type'] is 'ied':
                    Ied.define_ied_dt(
                        item, temp_variable_dict[item], serverClient.variables, component)

        with app.app_context():
            turbo.push(turbo.replace(render_template(
                'components.html', origins=serverClient.sort_by_origin()), 'load-components'))
            turbo.push(turbo.replace(render_template(
                'timestamp.html', timestamp=f'Cycle: {str(cycle)}'), 'load-timestamp'))


@app.route("/")
def home():
    return render_template('index.html')


@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()


def update_load():
    global serverClient
    with app.app_context():
        # --------------------- SERVER --------------------------
        if current_source == 'mqtt':
            serverClient = ServerClient(
                '139.59.97.171', 1883, 'measures/#', on_connect, on_message)
            serverClient.connect()

            # Variable to be read in onMessage
            try:
                while True:
                    time.sleep(1)

            except KeyboardInterrupt:
                serverClient.server.disconnect()
                serverClient.server.loop_stop()
        # --------------------- SERVER END --------------------------

        # --------------------- TEXT LOGS --------------------------
        elif current_source == 'log':
            serverClient = ServerClient()
            f = open(DATA + 'mqttlog.txt', 'r')
            line_counter = 0
            cycle = 0
            for line in f.readlines():

                dt_item = json.loads(line)[0]

                # Get the name of the component.
                name = dt_item['value'][(dt_item['value'].find(
                    ']') + 1): dt_item['value'].find(':')].strip()

                # To find the component and element split point.
                c_index = len(name) - 1
                for c in name[::-1]:
                    if c == '_':
                        break
                    c_index -= 1

                component = name[0: c_index]
                element = name[c_index + 1: len(name)]

                # Get the value of the component.
                value = float(dt_item['value'][dt_item['value'].find(
                    ':')+1: len(dt_item['value'])].strip())

                if component in temp_variable_dict:
                    temp_variable_dict[component][element] = value
                else:
                    temp_variable_dict[component] = {element: value}

                line_counter += 1

                # Each MQTT call give us 79 line of logs, each 79 lines represents a second/round in dt.
                if line_counter >= 79:
                    line_counter = 0
                    cycle += 1
                    for component, component_val in DT_VALUES.items():
                        for item, item_val in component_val.items():
                            if item_val['type'] is 'switch':
                                Switch.define_switch_dt(
                                    item, temp_variable_dict[item], serverClient.variables, component)
                            elif item_val['type'] is 'ied':
                                Ied.define_ied_dt(
                                    item, temp_variable_dict[item], serverClient.variables, component)

                    turbo.push(turbo.replace(render_template(
                        'components.html', origins=serverClient.sort_by_origin()), 'load-components'))
                    turbo.push(turbo.replace(render_template(
                        'timestamp.html', timestamp=f'Cycle: {str(cycle)}'), 'load-timestamp'))

                    time.sleep(1)
            # --------------------- TEXT LOGS END --------------------------
        else:
            print('Please set proper current mode')
            exit()


if __name__ == "__main__":
    app.run(debug=True)
    # main()
