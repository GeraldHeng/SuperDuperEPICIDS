# https://diyprojects.io/flask-bootstrap-html-interface-effortless-python-projects/#.YNnlLhMza3I
# https://blog.miguelgrinberg.com/post/dynamically-update-your-flask-web-pages-using-turbo-flask
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

app = Flask(__name__)
turbo = Turbo(app)
logs = []


class ServerClient:
    def __init__(self, server_ip, port, topic, on_connect, on_message):
        self.variables = {}
        self.server = mqttClient.Client('client')
        self.broker_address = server_ip
        self.port = port
        self.topic = topic

        self.server.on_connect = on_connect
        self.server.on_message = on_message

    def connect(self):
        print('connecting')
        self.server.connect(self.broker_address, port=self.port)
        self.server.loop_start()
        time.sleep(2)
        self.server.subscribe(self.topic)

    # OK
    def check_case_smart_home(self):
        '''
        The summation of TIED2 and TIED4 should be equal to the summation of SIED1 to 4
        absolute((TIED2 + TIED4) - (SIED1 + SIED2 + SIED3 + SIED4)) <= CURRENT MARGIN
        '''
        tied_sum = 0
        sied_sum = 0

        # TIED2
        if self.variables['q3'].is_switch_close():
            tied_sum += self.variables['tied2'].current

        # TIED4
        if self.variables['q2-1'].is_switch_close():
            tied_sum += self.variables['tied4'].current

        # SIED 1,2,3,4
        i = 3
        for x in range(1, 5):
            if self.variables['q3-' + str(x + i)].is_switch_close():
                sied_sum += self.variables['sied' + str(x)].current

            i = i - 2

        if np.less(abs(tied_sum - sied_sum), CURRENT_MARGIN).all():
            # print(Fore.GREEN + 'Case Smart Home is consistent')
            return True
        else:
            if self.variables['q3'].is_switch_close():
                self.variables['tied2'].consistent_status = False
                self.variables['tied2'].consistency_message = 'Inconsistent with Case Smart Home'

            if self.variables['q2-1'].is_switch_close():
                self.variables['tied4'].consistent_status = False
                self.variables['tied4'].consistency_message = 'Inconsistent with Case Smart Home'

            i = 3
            for x in range(1, 5):
                if self.variables['q3-' + str(x + i)].is_switch_close():
                    self.variables['sied' + str(x)].consistent_status = False
                    self.variables['sied' +
                                   str(x)].consistency_message = 'Inconsistent with Case Smart Home'
                i = i - 2

            print(Fore.RED + 'Case Smart Home is NOT consistent')
            print('tied_sum Value ' + str(tied_sum))
            print('sied_sum Value ' + str(sied_sum))
            print('abs', abs(tied_sum - sied_sum))
            print()
            return False

    # HALF OK, need to add MAMI3
    def check_case_micro_grid(self):
        '''
        The summation of TIED4 should be equal to the summation of MIED1, MIED2,
        25A(Q2) and 63A(Q2A) depending on switch status.
        absolute( TIED4 - (MIED1 + MIED2 + 25A(Q2) + 63A(Q2A))) <= CURRENT MARGIN
        '''
        tied_sum = 0
        mied_sum = 0

        # TIED4
        if self.variables['q2-1'].is_switch_close():
            tied_sum += self.variables['tied4'].current

        # 25A(Q2)
        # if self.variables['q2'].is_switch_close():
        #     mied_sum += 25

        # # 63A(Q2A)
        # if self.variables['q2a'].is_switch_close():
        #     mied_sum += 63

        # MIED1
        if self.variables['q2b'].is_switch_close():
            mied_sum += self.variables['mied1'].current

        # MIED2
        if self.variables['q2c'].is_switch_close():
            mied_sum += self.variables['mied2'].current

        if np.less(abs(tied_sum - mied_sum), CURRENT_MARGIN).all():
            # print(Fore.GREEN + 'Case Micro Grid is consistent')
            # print()
            return True
        else:
            if self.variables['q2-1'].is_switch_close():
                self.variables['tied4'].consistent_status = False
                self.variables['tied4'].consistency_message = 'Inconsistent with Case Micro Grid'

            if self.variables['q2b'].is_switch_close():
                self.variables['mied1'].consistent_status = False
                self.variables['mied1'].consistency_message = 'Inconsistent with Case Micro Grid'

            if self.variables['q2c'].is_switch_close():
                self.variables['mied2'].consistent_status = False
                self.variables['mied2'].consistency_message = 'Inconsistent with Case Micro Grid'

            print(Fore.RED + 'Case Micro Grid is NOT consistent')
            print('tied_sum Value ' + str(tied_sum))
            print('mied_sum Value ' + str(mied_sum))
            print('abs', abs(tied_sum - mied_sum))
            print()
            return False

    # NOT OK
    def check_case_generation(self):
        '''
        The summation of GIED2, GIED1 divided by amount of pathways (1 to 4)
        should be equal to TIED1.
        absolute(((GIED1 + GIED2) / outlet_switch_close_count) - tied_sum) <= CURRENT MARGIN
        outlet_switch_close_count - amount of switches that is close.
        '''
        tied_sum = 0
        gied_sum = 0
        outlet_switch_close_count = 0

        # GIED1
        if self.variables['q1'].is_switch_close():
            gied_sum += self.variables['gied1'].current

        # GIED2
        if self.variables['q1a'].is_switch_close():
            gied_sum += self.variables['gied2'].current

        # Q1-1
        if self.variables['q1-1'].is_switch_close():
            outlet_switch_close_count += 1

        # Q1-2
        if self.variables['q1-2'].is_switch_close():
            outlet_switch_close_count += 1

        # TIED1
        if self.variables['q1-3'].is_switch_close():
            print('wow it is close')
            outlet_switch_close_count += 1
            tied_sum += self.variables['tied1'].current

        # Q1-4
        # if self.variables['q1-4'].is_switch_close():
        #     outlet_switch_close_count += 1

        # print('outlet_switch_close_count', outlet_switch_close_count)
        if outlet_switch_close_count > 0:
            result = abs((gied_sum/outlet_switch_close_count))
        else:
            result = 0

        if self.variables['q1-3'].is_switch_close():
            if np.less((result - tied_sum), CURRENT_MARGIN).all():
                # print(Fore.GREEN + 'Case Generation is consistent')
                # print()
                self.check_case_extended_generation(
                    gied_sum, outlet_switch_close_count)
                return True
            else:
                print(Fore.RED + 'Case Generation is NOT consistent')
                print('result', result)
                print('tied_sum', tied_sum)
                # print(outlet_switch_close_count)
                print()
                self.check_case_extended_generation(
                    gied_sum, outlet_switch_close_count)

                return False
        else:
            print(
                Fore.YELLOW + 'Case Generation not called as TIED1 Switch, Q1-3 is OFF, case not able to check')
            print()
            return True

    # NOT OK
    def check_case_extended_generation(self, generation_sum, outlet_switch_close_count):
        '''
        Case Extended Generation: Need value outlet_switch_close_count and gied_sum from Case Generation.

        If Q2C and Q1-2 is ON(CLOSE), gied_sum divided by amount of
        outlet_switch_close_count should be equal to MIED2.

        If Q2B and Q1-1 is ON(CLOSE), gied_sum divided by amount of
        outlet_switch_close_count should be equal to MIED1.
        '''

        if outlet_switch_close_count > 0:
            generationValue = generation_sum / outlet_switch_close_count
        else:
            generationValue = 0
        # generationValue = generation_sum / outlet_switch_close_count

        # Q2C and Q1-2.
        if (self.variables['q2c'].is_switch_close() and
                self.variables['q1-2'].is_switch_close()):
            if np.less(abs(self.variables['mied2'].current - generationValue),
                       CURRENT_MARGIN).all():
                # print(Fore.GREEN + 'Case Extended Generation MIED2 is consistent')
                # print()
                return True
            else:
                print(Fore.RED + 'Case Extended Generation MIED2 is NOT consistent')
                print()
                return False
        else:
            print(
                Fore.YELLOW + 'Case Extended Generation MIED2 not called, switches not ON(CLOSE)')
            print()
            return True

        # Q2B and Q1-1.
        if (self.variables['q2b'].is_switch_close() and
                self.variables['q1-1'].is_switch_close()):
            if np.less(abs(self.variables['mied1'].current - generationValue),
                       CURRENT_MARGIN).all():
                # print(Fore.GREEN + 'Case Extended Generation MIED1 is consistent')
                # print()
                return True
            else:
                print(Fore.RED + 'Case Extended Generation MIED1 is NOT consistent')
                print()
                return False
        else:
            print(
                Fore.YELLOW + 'Case Extended Generation MIED1 not called, switches not ON(CLOSE)')
            print()
            return True

    # OK
    def check_case_tied1_tied2(self):
        '''
        TIED1 should be equal to TIED2 If both switches, Q1-3 and Q3 are ON(CLOSE).
        '''
        # Q2C and Q1-2.
        if (self.variables['q1-3'].is_switch_close() and
                self.variables['q3'].is_switch_close()):
            if np.less(abs(self.variables['tied1'].current - self.variables['tied2'].current),
                       CURRENT_MARGIN).all():
                # print(Fore.GREEN + 'Case TIED1 TIED2 is consistent')
                # print()
                return True
            else:
                self.variables['tied1'].consistent_status = False
                self.variables['tied2'].consistency_message = 'Inconsistent with Case TIED1 TIED2'

                self.variables['tied1'].consistent_status = False
                self.variables['tied2'].consistency_message = 'Inconsistent with Case TIED1 TIED2'
                print(Fore.RED + 'Case TIED1 TIED2 is NOT consistent')
                print()
                return False
        else:
            print(
                Fore.YELLOW + 'Case TIED1 TIED2 not called, switches not ON(CLOSE)')
            print()
            return False

    # NOT NEEDED
    def check_case_sied1_gied2(self):
        '''
        SIED1 should be equal to GIED2 If both switches, Q3-4, Q1A are ON(CLOSE).
        '''
        # Q2C and Q1-2.
        if (self.variables['q3-4'].is_switch_close() and
                self.variables['q1a'].is_switch_close()):
            if np.less(abs(self.variables['sied1'].current - self.variables['gied2'].current),
                       CURRENT_MARGIN).all():
                # print(Fore.GREEN + 'Case SIED1 GIED2 is consistent')
                # print()
                return True
            else:
                print(Fore.RED + 'Case SIED1 GIED2 is NOT consistent')
                print('sied1', self.variables['sied1'].current)
                print('gied2', self.variables['gied2'].current)
                print('abs', abs(
                    self.variables['sied1'].current - self.variables['gied2'].current))
                print()
                return False
        else:
            print(
                Fore.YELLOW + 'Case SIED1 GIED2 not called, switches not ON(CLOSE)')
            print()
            return True

    def update_client_object(self):
        '''
        Get all items in server/client.
        '''
        helper.update_EPIC_Objects(self.server)
        # time.sleep(2)
        variables = self.get_data()

    def get_data(self):
        '''
        Update variables with all the switches and ieds.
        '''
        for component, component_val in VALUES.items():
            for item, item_val in component_val.items():
                if item_val['type'] is 'switch':
                    if 'connected_to' in item_val:
                        connected_to = item_val['connected_to']
                    else:
                        connected_to = None

                    Switch.define_switch((component + '.' + item.replace('-', '_')), helper.dict, item.lower(),
                                         self.variables, self.server, connected_to, component)
                elif item_val['type'] is 'ied':
                    Ied.define_ied((component + '.' + item.replace('-', '_')), helper.dict, item.lower(),
                                   self.variables, self.server, component)

        self.variables['timestamp'] = helper.get_node_value(
            'timestamp', self.server, helper.dict)

        return self.variables

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


def on_message(client, userdata, message):
    # print(message.payload.decode("utf-8"))
    global line_counter
    global temp_variable_dict
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

    print('component', component)
    print('element', element)
    print('value', value)

    line_counter += 1
    print('line counter', line_counter)

    if component in temp_variable_dict:
        temp_variable_dict[component][element] = value
    else:
        temp_variable_dict[component] = {element: value}

    if line_counter >= 79:
        line_counter = 0
        print('finish message interval')
        print(temp_variable_dict)

        for name, temp_var in temp_variable_dict.items():
            print(name)
            print(temp_var)
            if name[0] is 'Q':
                # Switch.define_switch_dt(name, val, variable_dict)
                print(name, 'is a switch')
            elif 'meter' in name.lower():
                # Ied.define_ied_dt(
                #     name, temp_variable_dict[name], variable_dict)
                print(name, 'is a ied')
            else:
                print(name, 'is G1, G2 or motor')

    # if component in temp_variable_dict:
    #     temp_variable_dict[component][element] = value
    # else:
    #     temp_variable_dict[component] = {element: value}

    # if name[0] is 'Q':
    #     Switch.define_switch_dt(name, val, variable_dict)
    #     print(name, 'is a switch')
    # elif 'meter' in name.lower():
    #     Ied.define_ied_dt(
    #         name, temp_variable_dict[name], variable_dict)
    #     print(name, 'is a ied')
    # else:
    #     print(name, 'is G1, G2 or motor')


# Count to 79 as each subscribe interval will have 79 message.
line_counter = 0
temp_variable_dict = {}


def main():
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

    # temp_variable_dict = {}
    # f = open(DATA + 'mqttlog.txt', 'r')
    # line_counter = 0
    # for line in f.readlines():

    #     dt_item = json.loads(line)[0]

    #     # Get the name of the component.
    #     name = dt_item['value'][(dt_item['value'].find(
    #         ']') + 1): dt_item['value'].find(':')].strip()

    #     # To find the component and element split point.
    #     c_index = len(name) - 1
    #     for c in name[::-1]:
    #         if c == '_':
    #             break
    #         c_index -= 1

    #     component = name[0: c_index]
    #     element = name[c_index + 1: len(name)]

    #     # Get the value of the component.
    #     value = float(dt_item['value'][dt_item['value'].find(
    #         ':')+1: len(dt_item['value'])].strip())

    #     if component in temp_variable_dict:
    #         temp_variable_dict[component][element] = value
    #     else:
    #         temp_variable_dict[component] = {element: value}

    #     line_counter += 1

    #     # Each MQTT call give us 79 line of logs, each 79 lines represents a second/round in dt.
    #     if line_counter >= 79:
    #         print()
    #         line_counter = 0
    #         variable_dict = {}
    #         for name, val in temp_variable_dict.items():
    #             if name[0] is 'Q':
    #                 Switch.define_switch_dt(name, val, variable_dict)
    #                 print(name, 'is a switch')
    #             elif 'meter' in name.lower():
    #                 Ied.define_ied_dt(
    #                     name, temp_variable_dict[name], variable_dict)
    #                 print(name, 'is a ied')
    #             else:
    #                 print(name, 'is G1, G2 or motor')

    #         print(variable_dict)

    #         time.sleep(1)

    # print(temp_variable_dict)
    # print('value is ', json.loads(dt_item['value']))

    # while 1:
    # serverClient.update_client_object()

    # print('\n' + Fore.CYAN + serverClient.get_timestamp() + '\n')
    # serverClient.check_all_variable_consistency()
    # case_smart_home = Case('Smart Home Check', 'current', 'summation_equal',
    #                        [[
    #                            serverClient.variables['tied2'], serverClient.variables['tied4']
    #                        ],
    #                            [
    #                            serverClient.variables['sied1'], serverClient.variables['sied2'],
    #                            serverClient.variables['sied3'], serverClient.variables['sied4'],
    #                        ]
    #                        ])
    # case_smart_home.get_result()
    # serverClient.check_case_smart_home()

    # serverClient.check_case_micro_grid()

    # serverClient.check_case_generation()

    # serverClient.check_case_tied1_tied2()
    # serverClient.check_case_sied1_gied2()
    # time.sleep(1)


@app.route("/")
def home():
    print(Ied)
    return render_template('index.html')


@app.route("/download-logs")
def download_logs():
    with open('data/logs.txt', 'w') as out_file:
        for log in logs:
            new_log = log.replace('<br/>', '\n')
            new_log += '\n'
            out_file.write(new_log)

    return send_file('data/logs.txt', as_attachment=True, attachment_filename="logs.txt")


# @app.before_first_request
# def before_first_request():
#     threading.Thread(target=update_load).start()


# def update_load():
#     with app.app_context():
#         serverClient = ServerClient('opc.tcp://0.0.0.0:4840')
#         serverClient.connect()
#         while True:
#             serverClient.update_client_object()
#             serverClient.check_all_variable_consistency()
#             serverClient.check_case_smart_home()
#             serverClient.check_case_micro_grid()
#             serverClient.check_case_tied1_tied2()

#             log = serverClient.get_timestamp()
#             for item in serverClient.variables.values():
#                 if (type(item) is Switch or type(item) is Ied) and item.consistent_status == False:
#                     log += ' <br/> ' + item.name + ' ' + item.consistency_message
#             logs.insert(0, log + ' <br/> ')

#             turbo.push(turbo.replace(render_template(
#                 'components.html', origins=serverClient.sort_by_origin()), 'load-components'))
#             turbo.push(turbo.replace(render_template(
#                 'timestamp.html', timestamp=serverClient.get_timestamp()), 'load-timestamp'))
#             turbo.push(turbo.replace(render_template(
#                 'logs.html', logs=logs), 'load-logs'))
#             time.sleep(0.5)


if __name__ == "__main__":
    # app.run(debug=True)
    main()
