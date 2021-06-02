'''
This is the minimal OPCUA server that mimics EPIC Testbed.
'''

from opcua import Server, ua
from random import uniform
import datetime
import time
import sys
import helper_functions.server_helper_funcs as madlad
import DataSets.Configs.IEDConfigs as IEDConfigs
import DataSets.Configs.AMIConfigs as AMIConfigs
import time


# Server Setup
# url = 'opc.tcp://192.168.1.103:4840'
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

print('Grid Sectors Are Set:\nMicroGrid: {}\nTransmission : {}\nGeneration : {}\nSmartHome : {}\n'.format(
    MicroGrid, Transmission, Generation, SmartHome))

# DB1
print('''
######################################################################################################################
############################################# Setting Up Sector : DB1 ################################################
######################################################################################################################
''')


print('Setting up DB1 Switches...')
Q1 = madlad.create_switch(
    EPIC, Generation, 'Generation.Q1', '[01]', False, True)  # 5
Q1A = madlad.create_switch(
    EPIC, Generation, 'Generation.Q1A', '[10]', True, False)  # 9
Q1_1 = madlad.create_switch(
    EPIC, Generation, 'Generation.Q1_1', '[01]', False, True)  # 13
Q1_2 = madlad.create_switch(
    EPIC, Generation, 'Generation.Q1_2', '[01]', False, True)  # 17
Q1_4 = madlad.create_switch(
    EPIC, Generation, 'Generation.Q1_4', '[01]', False, True)
Q1_5 = madlad.create_switch(
    EPIC, Generation, 'Generation.Q1_5', '[01]', False, True)
Q1_3 = madlad.create_switch(
    EPIC, Transmission, 'Transmission.Q1_3', '[10]', True, False)  # 21
print('DB1 Switches Are Set:\nQ1: {}\nQ1A: {}\nQ1_1: {}\nQ1_2: {}\nQ1_3: {}Q1_4: {}Q1_5: {}\n'.format(
    Q1, Q1A, Q1_1, Q1_2, Q1_3, Q1_4, Q1_5))


print('Setting up DB1 Meters...')
TIED1 = madlad.create_meter(EPIC, Transmission, 'Transmission.TIED1')  # 25
GIED1 = madlad.create_meter(EPIC, Generation, 'Generation.GIED1')  # 40
GIED2 = madlad.create_meter(EPIC, Generation, 'Generation.GIED2')  # 55
print('TIED1 : {}\nGIED1 : {}\nGIED2 : {}\n'.format(TIED1, GIED1, GIED2))
# Need to set the value field to the appropriate values.


# DB2
print('''
######################################################################################################################
############################################# Setting Up Sector : DB2 ################################################
######################################################################################################################
''')


print('Setting up DB2 Switches...')
Q2 = madlad.create_switch(
    EPIC, MicroGrid, 'MicroGrid.Q2', '[10]', True, False)  # 70
Q2A = madlad.create_switch(
    EPIC, MicroGrid, 'MicroGrid.Q2A', '[10]', True, False)  # 74
Q2B = madlad.create_switch(
    EPIC, MicroGrid, 'MicroGrid.Q2B', '[01]', False, True)  # 78
Q2C = madlad.create_switch(
    EPIC, MicroGrid, 'MicroGrid.Q2C', '[01]', False, True)  # 82
Q2_1 = madlad.create_switch(
    EPIC, Transmission, 'Transmission.Q2_1', '[01]', False, True)  # 86
print('DB2 Switches Are Set:\nQ2: {}\nQ2A: {}\nQ2B: {}\nQ2C: {}\nQ2_1: {}\n'.format(
    Q2, Q2A, Q2B, Q2C, Q2_1))


print('Setting up DB2 Meters...')
MIED1 = madlad.create_meter(EPIC, MicroGrid, 'MicroGrid.MIED1')  # 90
MIED2 = madlad.create_meter(EPIC, MicroGrid, 'MicroGrid.MIED2')  # 105
TIED4 = madlad.create_meter(EPIC, Transmission, 'Transmission.TIED4')  # 120
print('MIED1 : {}\nMIED2 : {}\nTIED4 : {}\n'.format(MIED1, MIED2, TIED4))
# Need to set the value field to the appropriate values.


print('Setting up DB2 AMI Meters...')
MAMI1 = madlad.create_AMIMeter(EPIC, MicroGrid, 'MicroGrid.MAMI1', '1')  # 135
MAMI2 = madlad.create_AMIMeter(EPIC, MicroGrid, 'MicroGrid.MAMI2', '2')  # 145
MAMI3 = madlad.create_AMIMeter(EPIC, MicroGrid, 'MicroGrid.MAMI3', '3')  # 155
print('MicroGrid AMI Meters Are Set:\nMAMI1: {}\nMAMI2: {}\nMAMI3: {}'.format(
    MAMI1, MAMI2, MAMI3))


# DB-3

print('''
######################################################################################################################
############################################# Setting Up Sector : DB3 ################################################
######################################################################################################################
\n''')
#
print('Setting up DB3 Switches')
Q3 = madlad.create_switch(
    EPIC, Transmission, 'Transmission.Q3', '[10]', True, False)  # 165
Q3_1 = madlad.create_switch(
    EPIC, SmartHome, 'SmartHome.Q3_1', '[10]', True, False)  # 169
Q3_2 = madlad.create_switch(
    EPIC, SmartHome, 'SmartHome.Q3_2', '[01]', False, True)  # 173
Q3_3 = madlad.create_switch(
    EPIC, SmartHome, 'SmartHome.Q3_3', '[10]', True, False)  # 177
Q3_4 = madlad.create_switch(
    EPIC, SmartHome, 'SmartHome.Q3_4', '[10]', True, False)  # 181
print('DB3 Switches Are Set:\nQ3: {}\nQ3_1: {}\nQ3_2: {}\nQ3_3: {}\nQ3_4: {}\n'.format(
    Q3, Q3_1, Q3_2, Q3_3, Q3_4))


print('Setting up DB3 Meters...')  # Haven't set up the values
TIED2 = madlad.create_meter(EPIC, Transmission, 'Transmission.TIED2')  # 185
SIED1 = madlad.create_meter(EPIC, SmartHome, 'SmartHome.SIED1')  # 200
SIED2 = madlad.create_meter(EPIC, SmartHome, 'SmartHome.SIED2')  # 215
SIED3 = madlad.create_meter(EPIC, SmartHome, 'SmartHome.SIED3')  # 230
SIED4 = madlad.create_meter(EPIC, SmartHome, 'SmartHome.SIED4')  # 245
print('TIED2 : {}\nSIED1 : {}\nSIED2 : {}\nSIED3 : {}\nSIED4 : {}\n'.format(
    TIED2, SIED1, SIED2, SIED3, SIED4))

# Only have some values for SAMI1 Meter. No Recorded Values for Other SAMI(#No) Meters.
print('Setting up DB3 AMI Meters...')
SAMI1 = madlad.create_AMIMeter(EPIC, MicroGrid, 'SmartHome.SAMI1', '1')  # 260
SAMI2 = madlad.create_AMIMeter(EPIC, MicroGrid, 'SmartHome.SAMI2', '2')  # 270
SAMI3 = madlad.create_AMIMeter(EPIC, MicroGrid, 'SmartHome.SAMI3', '3')  # 280
print('DB3 AMI Meters Are Set:\nSAMI1: {}\nSAMI2: {}\nSAMI3: {}'.format(
    SAMI1, SAMI2, SAMI3))

print('''
######################################################################################################################
################################################## Starting Server! ##################################################
######################################################################################################################
\n''')


try:
    server.start()
    print('Server Online')
    # embed()
    cycle = 0
    # embed()

    # print(MIED1.get_browse_name().to_string())
    while True:
        print('''
        ######################################################################################################################
        #################################################### Cycle No. {} #####################################################
        ######################################################################################################################
        \n'''.format(cycle))

        time.sleep(3)

        # set values for MIED
        madlad.setting_values(MIED1, IEDConfigs.update_IED(
            MIED1, IEDConfigs.MIED1), '1')

        madlad.setting_values(MIED2, IEDConfigs.update_IED(
            MIED2, IEDConfigs.MIED2), '2')
        # madlad.setting_values(TIED4, IConfigs.update_TIED('4', Configs.TIED4)) # Fix the values.

        # set values for AMI
        madlad.setting_values(MAMI1, AMIConfigs.update_AMI(
            MAMI1, AMIConfigs.MAMI1), '1')
        madlad.setting_values(MAMI2, AMIConfigs.update_AMI(
            MAMI2, AMIConfigs.MAMI2), '2')
        madlad.setting_values(MAMI3, AMIConfigs.update_AMI(
            MAMI3, AMIConfigs.MAMI3), '3')

        for var in MIED1.get_variables():
            print(var.get_browse_name().to_string(), var.get_value())

        cycle += 1

finally:
    server.stop()
    print('Server Offline')
