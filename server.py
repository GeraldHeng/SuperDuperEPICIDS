'''
This is the minimal OPCUA server that mimics EPIC Testbed.
'''

from opcua import Server, ua
from random import uniform
import datetime
import time
import sys
import helpers.server_helper_funcs as madlad
from helpers.constant import *
import csv

# Server Setup
url = 'opc.tcp://0.0.0.0:4840'
name = 'OPCUA_SIMULATION_SERVER'

server = Server()
server.set_endpoint(url)
EPIC = server.register_namespace(name)  # ns = 2

# Folder Objects
common = server.nodes.objects.add_folder(EPIC, "common")
components = VALUES
for component in components.keys():
    print(component)
    node = server.nodes.objects.add_folder(EPIC, component)
    components[component]['node_val'] = node

variable_dict = {}

# Timestamp
ts = madlad.create_timestamp(
    EPIC, common, 'common.', 'timestamp')  # 5
variable_dict['timestamp'] = ts

# All components inside SLD.
for component, component_val in VALUES.items():
    print('Setting up ' + component + '...')
    for item, item_val in component_val.items():
        if item != 'node_val':
            if item_val['type'] is SWITCH or item_val['type'] is IED:
                item_created = None
                item = item.replace('-', '_')

                if item_val['type'] is SWITCH:
                    item_created = madlad.create_switch(
                        EPIC, component_val['node_val'], (component + '.' + item))
                elif item_val['type'] is IED:
                    item_created = madlad.create_meter(
                        EPIC, component_val['node_val'], (component + '.' + item))

                if item_created is not None:
                    print(item.lower())
                    variable_dict[item.lower()] = item_created


# Might be useless...
# print('Setting up AMI Meters...')
MAMI1 = madlad.create_AMIMeter(
    EPIC, components['MicroGrid']['node_val'], 'MicroGrid.MAMI1', '1')  # 135
MAMI2 = madlad.create_AMIMeter(
    EPIC, components['MicroGrid']['node_val'], 'MicroGrid.MAMI2', '2')  # 145
MAMI3 = madlad.create_AMIMeter(
    EPIC, components['MicroGrid']['node_val'], 'MicroGrid.MAMI3', '3')  # 155
SAMI1 = madlad.create_AMIMeter(
    EPIC, components['SmartHome']['node_val'], 'SmartHome.SAMI1', '1')  # 260
SAMI2 = madlad.create_AMIMeter(
    EPIC, components['SmartHome']['node_val'], 'SmartHome.SAMI2', '2')  # 270
SAMI3 = madlad.create_AMIMeter(
    EPIC, components['SmartHome']['node_val'], 'SmartHome.SAMI3', '3')  # 280

try:
    print('Server Starting')
    server.start()
    print('Server Online')

    while 1:
        # chosen_scenario = int(input('Please select a scenario 1 - 8: '))
        select_num = 1
        data_list_items = DATA_LIST.items()
        for origin, data_list in data_list_items:
            print(origin + ":")
            for data in data_list:
                print(data['name'], 'Please select -', select_num)
                data['number'] = select_num
                select_num += 1
            print()

        chosen_data_number = int(input(('Please select data to read from - ')))

        chosen_data = None
        for origin, data_list in data_list_items:
            if not chosen_data:
                for data in data_list:
                    if data['number'] == chosen_data_number:
                        chosen_data = data
                        break

        if not chosen_data:
            print('Please select a valid path')
            continue

        # Open respective scenario file and run.
        print('--------------- Starting', data['name'], '---------------')
        if data['type'] == 're_csv':
            with open(data['path'], mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for line in csv_reader:
                    print(line['Timestamp'])
                    for key, value in variable_dict.items():
                        if key != 'timestamp':
                            madlad.setting_values(value, line)
                        else:
                            value.get_variables()[0].set_value(
                                line['Timestamp'])

                    time.sleep(1)
        elif data['type'] == 'dt_mqtt_txt':
            print('mqtt text file goes here')

finally:
    server.stop()
    print('Server Offline')
