'''
This is the minimal OPCUA server that mimics EPIC Testbed.
'''

from opcua import Server, ua
from random import uniform
import datetime
import time
import sys
import helpers.server_helper_funcs as madlad
import datasets.configs.ied_configs as IEDConfigs
import datasets.configs.ami_configs as AMIConfigs
import time
import constant
import csv

# Server Setup
url = 'opc.tcp://0.0.0.0:4840'
name = 'OPCUA_SIMULATION_SERVER'

server = Server()
server.set_endpoint(url)
EPIC = server.register_namespace(name)  # ns = 2

# Folder Object
MicroGrid = server.nodes.objects.add_folder(EPIC, "MicroGrid")  # 1
Transmission = server.nodes.objects.add_folder(EPIC, "Transmission")  # 2
Generation = server.nodes.objects.add_folder(EPIC, "Generation")  # 3
SmartHome = server.nodes.objects.add_folder(EPIC, "SmartHome")  # 4

variable_dict = {}

print('Setting up DB1 Switches...')
Q1 = madlad.create_switch(
    EPIC, Generation, 'Generation.Q1', '[01]', False, True)  # 5
variable_dict['q1'] = Q1
Q1A = madlad.create_switch(
    EPIC, Generation, 'Generation.Q1A', '[10]', True, False)  # 9
variable_dict['q1a'] = Q1A
Q1_1 = madlad.create_switch(
    EPIC, Generation, 'Generation.Q1_1', '[01]', False, True)  # 13
variable_dict['q1-1'] = Q1_1
Q1_2 = madlad.create_switch(
    EPIC, Generation, 'Generation.Q1_2', '[01]', False, True)  # 17
variable_dict['q1-2'] = Q1_2
Q1_4 = madlad.create_switch(
    EPIC, Generation, 'Generation.Q1_4', '[01]', False, True)
variable_dict['q1-4'] = Q1_4
Q1_5 = madlad.create_switch(
    EPIC, Generation, 'Generation.Q1_5', '[01]', False, True)
variable_dict['q1-5'] = Q1_5
Q1_3 = madlad.create_switch(
    EPIC, Transmission, 'Transmission.Q1_3', '[10]', True, False)  # 21
variable_dict['q1-3'] = Q1_3


print('Setting up DB1 Meters...')
TIED1 = madlad.create_meter(EPIC, Transmission, 'Transmission.TIED1')  # 25
variable_dict['tied1'] = TIED1
GIED1 = madlad.create_meter(EPIC, Generation, 'Generation.GIED1')  # 40
variable_dict['gied1'] = GIED1
GIED2 = madlad.create_meter(EPIC, Generation, 'Generation.GIED2')  # 55
variable_dict['gied2'] = GIED2


print('Setting up DB2 Switches...')
Q2 = madlad.create_switch(
    EPIC, MicroGrid, 'MicroGrid.Q2', '[10]', True, False)  # 70
variable_dict['q2'] = Q2
Q2A = madlad.create_switch(
    EPIC, MicroGrid, 'MicroGrid.Q2A', '[10]', True, False)  # 74
variable_dict['q2a'] = Q2A
Q2B = madlad.create_switch(
    EPIC, MicroGrid, 'MicroGrid.Q2B', '[01]', False, True)  # 78
variable_dict['q2b'] = Q2B
Q2C = madlad.create_switch(
    EPIC, MicroGrid, 'MicroGrid.Q2C', '[01]', False, True)  # 82
variable_dict['q2c'] = Q2C
Q2_1 = madlad.create_switch(
    EPIC, Transmission, 'Transmission.Q2_1', '[01]', False, True)  # 86
variable_dict['q2-1'] = Q2_1


print('Setting up DB2 Meters...')
MIED1 = madlad.create_meter(EPIC, MicroGrid, 'MicroGrid.MIED1')  # 90
variable_dict['mied1'] = MIED1
MIED2 = madlad.create_meter(EPIC, MicroGrid, 'MicroGrid.MIED2')  # 105
variable_dict['mied2'] = MIED2
TIED4 = madlad.create_meter(EPIC, Transmission, 'Transmission.TIED4')  # 120
variable_dict['tied4'] = TIED4


print('Setting up DB2 AMI Meters...')
MAMI1 = madlad.create_AMIMeter(EPIC, MicroGrid, 'MicroGrid.MAMI1', '1')  # 135
MAMI2 = madlad.create_AMIMeter(EPIC, MicroGrid, 'MicroGrid.MAMI2', '2')  # 145
MAMI3 = madlad.create_AMIMeter(EPIC, MicroGrid, 'MicroGrid.MAMI3', '3')  # 155


print('Setting up DB3 Switches')
Q3 = madlad.create_switch(
    EPIC, Transmission, 'Transmission.Q3', '[10]', True, False)  # 165
variable_dict['q3'] = Q3
Q3_1 = madlad.create_switch(
    EPIC, SmartHome, 'SmartHome.Q3_1', '[10]', True, False)  # 169
variable_dict['q3-1'] = Q3_1
Q3_2 = madlad.create_switch(
    EPIC, SmartHome, 'SmartHome.Q3_2', '[01]', False, True)  # 173
variable_dict['q3-2'] = Q3_2
Q3_3 = madlad.create_switch(
    EPIC, SmartHome, 'SmartHome.Q3_3', '[10]', True, False)  # 177
variable_dict['q3-3'] = Q3_3
Q3_4 = madlad.create_switch(
    EPIC, SmartHome, 'SmartHome.Q3_4', '[10]', True, False)  # 181
variable_dict['q3-4'] = Q3_4


print('Setting up DB3 Meters...')  # Haven't set up the values
TIED2 = madlad.create_meter(EPIC, Transmission, 'Transmission.TIED2')  # 185
variable_dict['tied2'] = TIED2
SIED1 = madlad.create_meter(EPIC, SmartHome, 'SmartHome.SIED1')  # 200
variable_dict['sied1'] = SIED1
SIED2 = madlad.create_meter(EPIC, SmartHome, 'SmartHome.SIED2')  # 215
variable_dict['sied2'] = SIED2
SIED3 = madlad.create_meter(EPIC, SmartHome, 'SmartHome.SIED3')  # 230
variable_dict['sied3'] = SIED3
SIED4 = madlad.create_meter(EPIC, SmartHome, 'SmartHome.SIED4')  # 245
variable_dict['sied4'] = SIED4


print('Setting up DB3 AMI Meters...')
SAMI1 = madlad.create_AMIMeter(EPIC, MicroGrid, 'SmartHome.SAMI1', '1')  # 260
SAMI2 = madlad.create_AMIMeter(EPIC, MicroGrid, 'SmartHome.SAMI2', '2')  # 270
SAMI3 = madlad.create_AMIMeter(EPIC, MicroGrid, 'SmartHome.SAMI3', '3')  # 280


try:
    print('Server Starting')
    server.start()
    print('Server Online')

    while 1:
        chosen_scenario_path = ''
        chosen_scenario = int(input('Please select a scenario 1 - 8: '))

        if chosen_scenario == 1:
            chosen_scenario_path = constant.SCENARIO_1_PATH
        elif chosen_scenario == 2:
            chosen_scenario_path = constant.SCENARIO_2_PATH
        elif chosen_scenario == 3:
            chosen_scenario_path = constant.SCENARIO_3_PATH
        elif chosen_scenario == 4:
            chosen_scenario_path = constant.SCENARIO_4_PATH
        elif chosen_scenario == 5:
            chosen_scenario_path = constant.SCENARIO_5_PATH
        elif chosen_scenario == 6:
            chosen_scenario_path = constant.SCENARIO_6_PATH
        elif chosen_scenario == 7:
            chosen_scenario_path = constant.SCENARIO_7_PATH
        elif chosen_scenario == 8:
            chosen_scenario_path = constant.SCENARIO_8_PATH
        else:
            print('Please select a valid path')
            continue

        with open(chosen_scenario_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                print(line['Timestamp'])
                # madlad.setting_values(MIED1, line, '1')

                for item in variable_dict.values():
                    madlad.setting_values(item, line, '1')
                    for var in item.get_variables():
                        if 'MicroGrid.MIED1.Measurement.V3' in var.get_browse_name().to_string():
                            print('MicroGrid.MIED1.Measurement.V3 data')
                            print(var.get_browse_name().to_string()
                                  [2:], var.get_value())

                time.sleep(1)
finally:
    server.stop()
    print('Server Offline')
