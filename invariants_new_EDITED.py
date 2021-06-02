import time
# import pythoncom
import OpenOPC as opc
import numpy as np
from colorama import init, Fore, Back, Style

_DEB = 'printall'
_DEB = ''
_ENV = '1line'
_ENV = ''

init(autoreset=True)
# opc = OpenOPC.open_client('opc.tcp://0.0.0.0:4840')
# opc = OpenOPC.client()
# server = 'SV.OPCDAServer'
# server = 'opc.tcp://0.0.0.0:4840'
print(opc.servers())

def connect(server):
    try:
        opc.connect(server)
        print(Fore.CYAN + "Connected to "+server)
    except:
        print(Fore.RED + "Connection to " + server + " failed")


def get_data():
    var = {}
    # SW
    var['m1'] = 1 if opc['MicroGrid.Q2B.STATUS_CLOSE'] else 0
    var['m2'] = 1 if opc['MicroGrid.Q2C.STATUS_CLOSE'] else 0
    var['bat'] = 1 if opc['MicroGrid.Q2.STATUS_CLOSE'] else 0
    var['pv'] = 1 if opc['MicroGrid.Q2A.STATUS_CLOSE'] else 0
    var['t4'] = 1 if opc['Transmission.Q2_1.STATUS_CLOSE'] else 0
    var['s1'] = 1 if opc['SmartHome.Q3_4.STATUS_CLOSE'] else 0
    var['s2'] = 1 if opc['SmartHome.Q3_3.STATUS_CLOSE'] else 0
    var['s3'] = 1 if opc['SmartHome.Q3_2.STATUS_CLOSE'] else 0
    var['s4'] = 1 if opc['SmartHome.Q3_1.STATUS_CLOSE'] else 0

    # EditedByNicholasAndTinkit
    var['g1'] = 1 if opc['Generation.Q1.STATUS_CLOSE'] else 0
    var['g2'] = 1 if opc['Generation.Q1A.STATUS_CLOSE'] else 0
    var['g3'] = 1 if opc['Generation.Q1_1.STATUS_CLOSE'] else 0
    var['g4'] = 1 if opc['Generation.Q1_2.STATUS_CLOSE'] else 0
    var['t1'] = 1 if opc['Transmission.Q1_3.STATUS_CLOSE'] else 0
    var['t2'] = 1 if opc['Transmission.Q3.STATUS_CLOSE'] else 0

    # SW_
    var['m1_'] = 0 if opc['MicroGrid.Q2B.STATUS_OPEN'] else 1
    var['m2_'] = 0 if opc['MicroGrid.Q2C.STATUS_OPEN'] else 1
    var['bat_'] = 0 if opc['MicroGrid.Q2.STATUS_OPEN'] else 1
    var['pv_'] = 0 if opc['MicroGrid.Q2A.STATUS_OPEN'] else 1
    var['t4_'] = 0 if opc['Transmission.Q2_1.STATUS_OPEN'] else 1
    var['s1_'] = 0 if opc['SmartHome.Q3_4.STATUS_OPEN'] else 1
    var['s2_'] = 0 if opc['SmartHome.Q3_3.STATUS_OPEN'] else 1
    var['s3_'] = 0 if opc['SmartHome.Q3_2.STATUS_OPEN'] else 1
    var['s4_'] = 0 if opc['SmartHome.Q3_1.STATUS_OPEN'] else 1

    # EditedByNicholasAndTinkit
    var['g1_'] = 0 if opc['Generation.Q1.STATUS_OPEN'] else 1
    var['g2_'] = 0 if opc['Generation.Q1A.STATUS_OPEN'] else 1
    var['g3_'] = 0 if opc['Generation.Q1_1.STATUS_OPEN'] else 1
    var['g4_'] = 0 if opc['Generation.Q1_2.STATUS_OPEN'] else 1
    var['t1_'] = 0 if opc['Transmission.Q1_3.STATUS_OPEN'] else 1
    var['t2_'] = 0 if opc['Transmission.Q3.STATUS_OPEN'] else 1

    # SW_ui
    var['m1_ui'] = opc['MicroGrid.Q2B.STATUS']
    var['m2_ui'] = opc['MicroGrid.Q2C.STATUS']
    var['bat_ui'] = opc['MicroGrid.Q2.STATUS']
    var['pv_ui'] = opc['MicroGrid.Q2A.STATUS']
    var['t4_ui'] = opc['Transmission.Q2_1.STATUS']
    var['s1_ui'] = opc['SmartHome.Q3_4.STATUS']
    var['s2_ui'] = opc['SmartHome.Q3_3.STATUS']
    var['s3_ui'] = opc['SmartHome.Q3_2.STATUS']
    var['s4_ui'] = opc['SmartHome.Q3_1.STATUS']

    # EditedByNicholasAndTinkit
    var['g1_ui'] = opc['Generation.Q1.STATUS']
    var['g2_ui'] = opc['Generation.Q1A.STATUS']
    var['g3_ui'] = opc['Generation.Q1_1.STATUS']
    var['g4_ui'] = opc['Generation.Q1_2.STATUS']
    var['t1_ui'] = opc['Transmission.Q1_3.STATUS']
    var['t2_ui'] = opc['Transmission.Q3.STATUS']

    # single face  or three face system - just take them all as a total current

    # I
    var['im1'] = np.array([opc['MicroGrid.MIED1.Measurement.L1_Current'],
                           opc['MicroGrid.MIED1.Measurement.L2_Current'], opc['MicroGrid.MIED1.Measurement.L3_Current']])
    var['im2'] = np.array([opc['MicroGrid.MIED2.Measurement.L1_Current'],
                           opc['MicroGrid.MIED2.Measurement.L2_Current'], opc['MicroGrid.MIED2.Measurement.L3_Current']])
    var['it4'] = np.array([opc['Transmission.TIED4.Measurement.L1_Current'],
                           opc['Transmission.TIED4.Measurement.L2_Current'], opc['Transmission.TIED4.Measurement.L3_Current']])
    var['is1'] = np.array([opc['SmartHome.SIED1.Measurement.L1_Current'],
                           opc['SmartHome.SIED1.Measurement.L2_Current'], opc['SmartHome.SIED1.Measurement.L3_Current']])
    var['is2'] = np.array([opc['SmartHome.SIED2.Measurement.L1_Current'],
                           opc['SmartHome.SIED2.Measurement.L2_Current'], opc['SmartHome.SIED2.Measurement.L3_Current']])
    var['is3'] = np.array([opc['SmartHome.SIED3.Measurement.L1_Current'],
                           opc['SmartHome.SIED3.Measurement.L2_Current'], opc['SmartHome.SIED3.Measurement.L3_Current']])
    var['is4'] = np.array([opc['SmartHome.SIED4.Measurement.L1_Current'],
                           opc['SmartHome.SIED4.Measurement.L2_Current'], opc['SmartHome.SIED4.Measurement.L3_Current']])

    # EditedByNicholasAndTinkit
    var['it2'] = np.array([opc['Transmission.TIED2.Measurement.L1_Current'],
                           opc['Transmission.TIED2.Measurement.L2_Current'], opc['Transmission.TIED2.Measurement.L3_Current']])
    var['it1'] = np.array([opc['Transmission.TIED1.Measurement.L1_Current'],
                           opc['Transmission.TIED1.Measurement.L2_Current'], opc['Transmission.TIED1.Measurement.L3_Current']])
    var['ig2'] = np.array([opc['Generation.GIED2.Measurement.L1_Current'],
                           opc['Generation.GIED2.Measurement.L2_Current'], opc['Generation.GIED2.Measurement.L3_Current']])
    var['ig1'] = np.array([opc['Generation.GIED1.Measurement.L1_Current'],
                           opc['Generation.GIED1.Measurement.L2_Current'], opc['Generation.GIED1.Measurement.L3_Current']])

    # V
    var['vm1'] = np.array([opc['MicroGrid.MIED1.Measurement.V1'], opc['MicroGrid.MIED1.Measurement.V2'], opc['MicroGrid.MIED1.Measurement.V3'],
                           opc['MicroGrid.MIED1.Measurement.VL1_L2'], opc['MicroGrid.MIED1.Measurement.VL2_L3'], opc['MicroGrid.MIED1.Measurement.VL3_VL1']])
    var['vm2'] = np.array([opc['MicroGrid.MIED2.Measurement.V1'], opc['MicroGrid.MIED2.Measurement.V2'], opc['MicroGrid.MIED2.Measurement.V3'],
                           opc['MicroGrid.MIED2.Measurement.VL1_L2'], opc['MicroGrid.MIED2.Measurement.VL2_L3'], opc['MicroGrid.MIED2.Measurement.VL3_VL1']])
    var['vt4'] = np.array([opc['Transmission.TIED4.Measurement.V1'], opc['Transmission.TIED4.Measurement.V2'], opc['Transmission.TIED4.Measurement.V3'],
                           opc['Transmission.TIED4.Measurement.VL1_L2'], opc['Transmission.TIED4.Measurement.VL2_L3'], opc['Transmission.TIED4.Measurement.VL3_VL1']])
    var['vs1'] = np.array([opc['SmartHome.SIED1.Measurement.V1'], opc['SmartHome.SIED1.Measurement.V2'], opc['SmartHome.SIED1.Measurement.V3'],
                           opc['SmartHome.SIED1.Measurement.VL1_L2'], opc['SmartHome.SIED1.Measurement.VL2_L3'], opc['SmartHome.SIED1.Measurement.VL3_VL1']])
    var['vs2'] = np.array([opc['SmartHome.SIED2.Measurement.V1'], opc['SmartHome.SIED2.Measurement.V2'], opc['SmartHome.SIED2.Measurement.V3'],
                           opc['SmartHome.SIED2.Measurement.VL1_L2'], opc['SmartHome.SIED2.Measurement.VL2_L3'], opc['SmartHome.SIED2.Measurement.VL3_VL1']])
    var['vs3'] = np.array([opc['SmartHome.SIED3.Measurement.V1'], opc['SmartHome.SIED3.Measurement.V2'], opc['SmartHome.SIED3.Measurement.V3'],
                           opc['SmartHome.SIED3.Measurement.VL1_L2'], opc['SmartHome.SIED3.Measurement.VL2_L3'], opc['SmartHome.SIED3.Measurement.VL3_VL1']])
    var['vs4'] = np.array([opc['SmartHome.SIED4.Measurement.V1'], opc['SmartHome.SIED4.Measurement.V2'], opc['SmartHome.SIED4.Measurement.V3'],
                           opc['SmartHome.SIED4.Measurement.VL1_L2'], opc['SmartHome.SIED4.Measurement.VL2_L3'], opc['SmartHome.SIED4.Measurement.VL3_VL1']])

    # EditedByNicholasAndTinkit
    var['vt2'] = np.array([opc['Transmission.TIED2.Measurement.V1'], opc['Transmission.TIED2.Measurement.V2'], opc['Transmission.TIED2.Measurement.V3'],
                           opc['Transmission.TIED2.Measurement.VL1_L2'], opc['Transmission.TIED2.Measurement.VL2_L3'], opc['Transmission.TIED2.Measurement.VL3_VL1']])
    var['vt1'] = np.array([opc['Transmission.TIED1.Measurement.V1'], opc['Transmission.TIED1.Measurement.V2'], opc['Transmission.TIED1.Measurement.V3'],
                           opc['Transmission.TIED1.Measurement.VL1_L2'], opc['Transmission.TIED1.Measurement.VL2_L3'], opc['Transmission.TIED1.Measurement.VL3_VL1']])
    var['vg2'] = np.array([opc['Generation.GIED2.Measurement.V1'], opc['Generation.GIED2.Measurement.V2'], opc['Generation.GIED2.Measurement.V3'],
                           opc['Generation.GIED2.Measurement.VL1_L2'], opc['Generation.GIED2.Measurement.VL2_L3'], opc['Generation.GIED2.Measurement.VL3_VL1']])
    var['vg1'] = np.array([opc['Generation.GIED1.Measurement.V1'], opc['Generation.GIED1.Measurement.V2'], opc['Generation.GIED1.Measurement.V3'],
                           opc['Generation.GIED1.Measurement.VL1_L2'], opc['Generation.GIED1.Measurement.VL2_L3'], opc['Generation.GIED1.Measurement.VL3_VL1']])

    # P
    var['papm1'] = np.array([opc['MicroGrid.MIED1.Measurement.Apparent']])
    var['prcm1'] = np.array([opc['MicroGrid.MIED1.Measurement.Reactive']])
    var['prlm1'] = np.array([opc['MicroGrid.MIED1.Measurement.Real']])
    var['papm2'] = np.array([opc['MicroGrid.MIED2.Measurement.Apparent']])
    var['prcm2'] = np.array([opc['MicroGrid.MIED2.Measurement.Reactive']])
    var['prlm2'] = np.array([opc['MicroGrid.MIED2.Measurement.Real']])
    var['papt4'] = np.array([opc['Transmission.TIED4.Measurement.Apparent']])
    var['prct4'] = np.array([opc['Transmission.TIED4.Measurement.Reactive']])
    var['prlt4'] = np.array([opc['Transmission.TIED4.Measurement.Real']])
    var['paps1'] = np.array([opc['SmartHome.SIED1.Measurement.Apparent']])
    var['prcs1'] = np.array([opc['SmartHome.SIED1.Measurement.Reactive']])
    var['prls1'] = np.array([opc['SmartHome.SIED1.Measurement.Real']])
    var['paps2'] = np.array([opc['SmartHome.SIED2.Measurement.Apparent']])
    var['prcs2'] = np.array([opc['SmartHome.SIED2.Measurement.Reactive']])
    var['prls2'] = np.array([opc['SmartHome.SIED2.Measurement.Real']])
    var['paps3'] = np.array([opc['SmartHome.SIED3.Measurement.Apparent']])
    var['prcs3'] = np.array([opc['SmartHome.SIED3.Measurement.Reactive']])
    var['prls3'] = np.array([opc['SmartHome.SIED3.Measurement.Real']])
    var['paps4'] = np.array([opc['SmartHome.SIED4.Measurement.Apparent']])
    var['prcs4'] = np.array([opc['SmartHome.SIED4.Measurement.Reactive']])
    var['prls4'] = np.array([opc['SmartHome.SIED4.Measurement.Real']])

    # EditedByNicholasAndTinkit
    var['papt2'] = np.array([opc['Transmission.TIED2.Measurement.Apparent']])
    var['prct2'] = np.array([opc['Transmission.TIED2.Measurement.Reactive']])
    var['prlt2'] = np.array([opc['Transmission.TIED2.Measurement.Real']])

    var['papt1'] = np.array([opc['Transmission.TIED1.Measurement.Apparent']])
    var['prct1'] = np.array([opc['Transmission.TIED1.Measurement.Reactive']])
    var['prlt1'] = np.array([opc['Transmission.TIED1.Measurement.Real']])

    var['papg2'] = np.array([opc['Generation.GIED2.Measurement.Apparent']])
    var['prcg2'] = np.array([opc['Generation.GIED2.Measurement.Reactive']])
    var['prlg2'] = np.array([opc['Generation.GIED2.Measurement.Real']])

    var['papg1'] = np.array([opc['Generation.GIED1.Measurement.Apparent']])
    var['prcg1'] = np.array([opc['Generation.GIED1.Measurement.Reactive']])
    var['prlg1'] = np.array([opc['Generation.GIED1.Measurement.Real']])

    return var


def mutate(var):
    # var[''] = var[''] + np.array([0, 0, 0]) + 0
    # var['im1'] = var['im1'] + np.array([0, 5, 0]) + 0
    return var


def print_arr(var):
    for x in var:
        print(str(x) + ': ' + str(var[x]))
    # print('papm1: ' + str(var['papm1']))
    # print('papm2: ' + str(var['papm2']))
    # print('papt4: ' + str(var['papt4']))
    # print('paps1: ' + str(var['paps1']))
    # print('paps2: ' + str(var['paps2']))
    # print('paps3: ' + str(var['paps3']))
    # print('paps4: ' + str(var['paps4']))


endc = True
delta = {}
delta['I'] = 0.5  # 0.45 3
delta['V'] = 4.5  # 10% 245 / 420
delta['P'] = 175  # 150 (2150)

# 11 values (11 sec) delay when switching on a switch
# 2 values (2 sec) delay when switching off a switch


try:
    connect(server)
    while endc:
        print(Fore.CYAN + time.asctime())
        var = get_data()
        var = mutate(var)

        # Invariants
        # Switch variable consistency

        # Q2B
        if var['m1'] == 0 and var['m1_'] == 0 and var['m1_ui'] == '[10]':
            print(Fore.GREEN + 'm1 consistency')
        elif var['m1'] == 1 and var['m1_'] == 1 and var['m1_ui'] == '[01]':
            print(Fore.GREEN + 'm1 consistency')
        else:
            print(Fore.RED + 'm1 consistency - m1: ' +
                  str(var['m1']) + ', m1_: ' + str(var['m1_']) + ', m1_ui: ' + str(var['m1_ui']))
        # Q2C
        if var['m2'] == 0 and var['m2_'] == 0 and var['m2_ui'] == '[10]':
            print(Fore.GREEN + 'm2 consistency')
        elif var['m2'] == 1 and var['m2_'] == 1 and var['m2_ui'] == '[01]':
            print(Fore.GREEN + 'm2 consistency')
        else:
            print(Fore.RED + 'm2 consistency - m2: ' +
                  str(var['m2']) + ', m2_: ' + str(var['m2_']) + ', m2_ui: ' + str(var['m1_ui']))
        # Q2-1
        if var['t4'] == 0 and var['t4_'] == 0 and var['t4_ui'] == '[10]':
            print(Fore.GREEN + 't4 consistency')
        elif var['t4'] == 1 and var['t4_'] == 1 and var['t4_ui'] == '[01]':
            print(Fore.GREEN + 't4 consistency')
        else:
            print(Fore.RED + 't4 consistency - t4: ' +
                  str(var['t4']) + ', t4_: ' + str(var['t4_']) + ', t4_ui: ' + str(var['t4_ui']))
        # Q3-4
        if var['s1'] == 0 and var['s1_'] == 0 and var['s1_ui'] == '[10]':
            print(Fore.GREEN + 's1 consistency')
        elif var['s1'] == 1 and var['s1_'] == 1 and var['s1_ui'] == '[01]':
            print(Fore.GREEN + 's1 consistency')
        else:
            print(Fore.RED + 's1 consistency - s1: ' +
                  str(var['s1']) + ', s1_: ' + str(var['s1_']) + ', s1_ui: ' + str(var['s1_ui']))
        # Q3-3
        if var['s2'] == 0 and var['s2_'] == 0 and var['s2_ui'] == '[10]':
            print(Fore.GREEN + 's2 consistency')
        elif var['s2'] == 1 and var['s2_'] == 1 and var['s2_ui'] == '[01]':
            print(Fore.GREEN + 's2 consistency')
        else:
            print(Fore.RED + 's2 consistency - s2: ' +
                  str(var['s2']) + ', s2_: ' + str(var['s2_']) + ', s2_ui: ' + str(var['s2_ui']))
        # Q3-2
        if var['s3'] == 0 and var['s3_'] == 0 and var['s3_ui'] == '[10]':
            print(Fore.GREEN + 's3 consistency')
        elif var['s3'] == 1 and var['s3_'] == 1 and var['s3_ui'] == '[01]':
            print(Fore.GREEN + 's3 consistency')
        else:
            print(Fore.RED + 's3 consistency - s3: ' +
                  str(var['s3']) + ', s3_: ' + str(var['s3_']) + ', s3_ui: ' + str(var['s3_ui']))
        # Q3-1
        if var['s4'] == 0 and var['s4_'] == 0 and var['s4_ui'] == '[10]':
            print(Fore.GREEN + 's4 consistency')
        elif var['s4'] == 1 and var['s4_'] == 1 and var['s4_ui'] == '[01]':
            print(Fore.GREEN + 's4 consistency')
        else:
            print(Fore.RED + 's4 consistency - s4: ' +
                  str(var['s4']) + ', s4_: ' + str(var['s4_']) + ', s4_ui: ' + str(var['s4_ui']))

        # EditedByNicholas&TinKit
        # Q2A
        if var['pv'] == 0 and var['pv_'] == 0 and var['pv_ui'] == '[10]':
            print(Fore.GREEN + 'pv consistency')
        elif var['pv'] == 1 and var['pv_'] == 1 and var['pv_ui'] == '[01]':
            print(Fore.GREEN + 'pv consistency')
        else:
            print(Fore.RED + 'pv consistency - pv: ' +
                  str(var['pv']) + ', pv_: ' + str(var['pv_']) + ', pv_ui: ' + str(var['pv_ui']))
        # Q2
        if var['bat'] == 0 and var['bat_'] == 0 and var['bat_ui'] == '[10]':
            print(Fore.GREEN + 'bat consistency')
        elif var['bat'] == 1 and var['bat_'] == 1 and var['bat_ui'] == '[01]':
            print(Fore.GREEN + 'bat consistency')
        else:
            print(Fore.RED + 'bat consistency - bat: ' + str(var['bat']) + ', bat_: ' + str(
                var['bat_']) + ', bat_ui: ' + str(var['bat_ui']))
        # Q1
        if var['g1'] == 0 and var['g1_'] == 0 and var['g1_ui'] == '[10]':
            print(Fore.GREEN + 'g1 consistency')
        elif var['g1'] == 1 and var['g1_'] == 1 and var['g1_ui'] == '[01]':
            print(Fore.GREEN + 'g1 consistency')
        else:
            print(Fore.RED + 'g1 consistency - g1: ' +
                  str(var['g1']) + ', g1_: ' + str(var['g1_']) + ', g1_ui: ' + str(var['g1_ui']))
        # Q1A
        if var['g2'] == 0 and var['g2_'] == 0 and var['g2_ui'] == '[10]':
            print(Fore.GREEN + 'g2 consistency')
        elif var['g2'] == 1 and var['g2_'] == 1 and var['g2_ui'] == '[01]':
            print(Fore.GREEN + 'g2 consistency')
        else:
            print(Fore.RED + 'g2 consistency - g2: ' +
                  str(var['g2']) + ', g2_: ' + str(var['g2_']) + ', g2_ui: ' + str(var['g2_ui']))
        # Q1-1
        if var['g3'] == 0 and var['g3_'] == 0 and var['g3_ui'] == '[10]':
            print(Fore.GREEN + 'g3 consistency')
        elif var['g3'] == 1 and var['g3_'] == 1 and var['g3_ui'] == '[01]':
            print(Fore.GREEN + 'g3 consistency')
        else:
            print(Fore.RED + 'g3 consistency - g3: ' +
                  str(var['g3']) + ', g3_: ' + str(var['g3_']) + ', g3_ui: ' + str(var['g3_ui']))
        # Q1-2
        if var['g4'] == 0 and var['g4_'] == 0 and var['g4_ui'] == '[10]':
            print(Fore.GREEN + 'g4 consistency')
        elif var['g4'] == 1 and var['g4_'] == 1 and var['g4_ui'] == '[01]':
            print(Fore.GREEN + 'g4 consistency')
        else:
            print(Fore.RED + 'g4 consistency - g4: ' +
                  str(var['g4']) + ', g4_: ' + str(var['g4_']) + ', g4_ui: ' + str(var['g4_ui']))
        # Q1-3
        if var['t1'] == 0 and var['t1_'] == 0 and var['t1_ui'] == '[10]':
            print(Fore.GREEN + 't1 consistency')
        elif var['t1'] == 1 and var['t1_'] == 1 and var['t1_ui'] == '[01]':
            print(Fore.GREEN + 't1 consistency')
        else:
            print(Fore.RED + 't1 consistency - t1: ' +
                  str(var['t1']) + ', t1_: ' + str(var['t1_']) + ', t1_ui: ' + str(var['t1_ui']))
        # Q3
        if var['t2'] == 0 and var['t2_'] == 0 and var['t2_ui'] == '[10]':
            print(Fore.GREEN + 't2 consistency')
        elif var['t2'] == 1 and var['t2_'] == 1 and var['t2_ui'] == '[01]':
            print(Fore.GREEN + 't2 consistency')
        else:
            print(Fore.RED + 't2 consistency - t2: ' +
                  str(var['t2']) + ', t2_: ' + str(var['t2_']) + ', t2_ui: ' + str(var['t2_ui']))

        # TODO:V sw OFF 
        # V sw OFF
		# All except TIED 4 will need to check their corresponding switch is open, then Voltage is near 0.
		# OFF means open hence [01]
        # Q2B,Q2C,Q2,Q2A = OPEN -> TIED4 VOLTAGE == 0

		# Why a whole micro grid and not m1 and m2 and t4 on its own?
        if var['m1'] == 0 and var['m2'] == 0 and var['bat'] == 0 and var['pv'] == 0:
            if np.less(abs(var['vt4']), delta['V']).all():
                print(Fore.GREEN + 'MicroGrid is OFF')
            else:
                print(Fore.RED + 'MicroGrid is OFF - vt4: ' + str(var['vt4']))

        # Q3-4 = OPEN -> SIED1 == 0
        if var['s1'] == 0:
            if np.less(abs(var['vs1']), delta['V']).all():
                print(Fore.GREEN + 'SIED1 is OFF: V')
            else:
                print(Fore.RED + 'SIED1 is OFF - vs1: ' + str(var['vs1']))
        # Q3-3 = OPEN -> SIED2 == 0
        if var['s2'] == 0:
            if np.less(abs(var['vs2']), delta['V']).all():
                print(Fore.GREEN + 'SIED2 is OFF: V')
            else:
                print(Fore.RED + 'SIED2 is OFF - vs2: ' + str(var['vs2']))
        # Q3-2 = OPEN -> SIED3 == 0
        if var['s3'] == 0:
            if np.less(abs(var['vs3']), delta['V']).all():
                print(Fore.GREEN + 'SIED3 is OFF: V')
            else:
                print(Fore.RED + 'SIED3 is OFF - vs3: ' + str(var['vs3']))
        # Q3-1 = OPEN -> SIED4 == 0
        if var['s4'] == 0:
            if np.less(abs(var['vs4']), delta['V']).all():
                print(Fore.GREEN + 'SIED4 is OFF: V')
            else:
                print(Fore.RED + 'SIED4 is OFF - vs4: ' + str(var['vs4']))

        # EditedByNicholas&TinKit
        # Q3 = OPEN -> TIED2 == 0
        if var['t2'] == 0:
            if np.less(abs(var['vt2']), delta['V']).all():
                print(Fore.GREEN + 'TIED2 is OFF: V')
            else:
                print(Fore.RED + 'TIED2 is OFF - vt2: ' + str(var['vt2']))
        # Q1A = OPEN -> GIED2 == 0
        if var['g2'] == 0:
            if np.less(abs(var['vg2']), delta['V']).all():
                print(Fore.GREEN + 'GIED2 is OFF: V')
            else:
                print(Fore.RED + 'GIED2 is OFF - vg2: ' + str(var['vg2']))
        # Q1 = OPEN -> GIED1 == 0
        if var['g1'] == 0:
            if np.less(abs(var['vg1']), delta['V']).all():
                print(Fore.GREEN + 'GIED1 is OFF: V')
            else:
                print(Fore.RED + 'GIED1 is OFF - vg1: ' + str(var['vg1']))
        # Q1-3 = OPEN -> TIED1 == 0
        if var['t1'] == 0:
            if np.less(abs(var['vt1']), delta['V']).all():
                print(Fore.GREEN + 'TIED1 is OFF: V')
            else:
                print(Fore.RED + 'TIED1 is OFF - vt1: ' + str(var['vt1']))


        # V sw ON

        # Q2B,Q2-1 = CLOSED -> TIED4 - MIED1 < V MARGIN
		# ----------------------------------------------------
		# Micro Grid, where the (TIED4) - (MIED1 + MIED 2) <= Voltage delta
		# Mirco Grid, One more case of if both m1 and m2 is closed (ON), then TIED4 - (MIED1 + MIED2)?
		# 3 switches involved. (Q2B, Q2C, Q2-1) 3^2 = 8cases?

		# m1 close m2 close t4 close
		# m1 close m2 close t4 open
		# m1 close m2 open t4 close
		# m1 close m2 open t4 open
		# m1 open m2 close t4 close
		# m1 open m2 open t4 close
		# m1 open m2 close t4 open
		# m1 open m2 open t4 open
        if var['m1'] == 1 and var['t4'] == 1:
            if np.less(abs(var['vt4'] - var['vm1']), delta['V']).all():
                print(Fore.GREEN + 'MIED1 is ON')
            else:
                print(Fore.RED + 'MIED1 is ON - vm1: ' +
                      str(var['vm1']) + ', vt4: ' + str(var['vt4']))
					  
        # Q2C,Q2-1 = CLOSED -> TIED4 - MIED2 < V MARGIN
        if var['m2'] == 1 and var['t4'] == 1:
            if np.less(abs(var['vt4'] - var['vm2']), delta['V']).all():
                print(Fore.GREEN + 'MIED2 is ON')
            else:
                print(Fore.RED + 'MIED2 is ON - vm2: ' +
                      str(var['vm2']) + ', vt4: ' + str(var['vt4']))

		# ---------------------------------------------------------


		# ---------------------------------------------------------
		# Smart home, where the (TIED2 + TIED4) - (SIED1 + SIED2 + SIED3 + SIED4) <= Voltage delta
		# 6 switches involved. (Q2-1, Q3-1, Q3-2, Q3-3, Q3-4, Q3) 6^2 = 64cases?
        # Q2-1,Q3-4 = CLOSED -> TIED4 - SIED1 < V MARGIN
        if var['t4'] == 1 and var['s1'] == 1:
            if np.less(abs(var['vt4'] - var['vs1']), delta['V']).all():
                print(Fore.GREEN + 'SIED1 is ON')
            else:
                print(Fore.RED + 'SIED1 is ON - vt4: ' +
                      str(var['vt4']) + ', vs1: ' + str(var['vs1']))

        # Q2-1,Q3-3 = CLOSED -> TIED4 - SIED2 < V MARGIN
        if var['t4'] == 1 and var['s2'] == 1:
            if np.less(abs(var['vt4'] - var['vs2']), delta['V']).all():
                print(Fore.GREEN + 'SIED2 is ON')
            else:
                print(Fore.RED + 'SIED2 is ON - vt4: ' +
                      str(var['vt4']) + ', vs2: ' + str(var['vs2']))

        # Q2-1,Q3-2 = CLOSED -> TIED4 - SIED3 < V MARGIN
        if var['t4'] == 1 and var['s3'] == 1:
            if np.less(abs(var['vt4'] - var['vs3']), delta['V']).all():
                print(Fore.GREEN + 'SIED3 is ON')
            else:
                print(Fore.RED + 'SIED3 is ON - vt4: ' +
                      str(var['vt4']) + ', vs3: ' + str(var['vs3']))

        # Q2-1,Q3-1 = CLOSED -> TIED4 - SIED4 < V MARGIN
        if var['t4'] == 1 and var['s4'] == 1:
            if np.less(abs(var['vt4'] - var['vs4']), delta['V']).all():
                print(Fore.GREEN + 'SIED4 is ON')
            else:
                print(Fore.RED + 'SIED4 is ON - vt4: ' +
                      str(var['vt4']) + ', vs4: ' + str(var['vs4']))

        # EditedByNicholas&TinKit
        # Q3,Q3-4 = CLOSED -> TIED2 - SIED1 < V MARGIN / IF Q2-1 OPEN
        if var['t2'] == 1 and var['s1'] == 1:
            if np.less(abs(var['vt2'] - var['vs1']), delta['V']).all():
                print(Fore.GREEN + 'SIED1 is ON')
            else:
                print(Fore.RED + 'SIED1 is ON - vt2: ' +
                      str(var['vt2']) + ', vs1: ' + str(var['vs1']))
        # Q3,Q3-3 = CLOSED -> TIED4 - SIED2 < V MARGIN / IF Q2-1 OPEN
        if var['t2'] == 1 and var['s2'] == 1:
            if np.less(abs(var['vt2'] - var['vs2']), delta['V']).all():
                print(Fore.GREEN + 'SIED2 is ON')
            else:
                print(Fore.RED + 'SIED2 is ON - vt2: ' +
                      str(var['vt2']) + ', vs2: ' + str(var['vs2']))
        # Q3,Q3-2 = CLOSED -> TIED4 - SIED3 < V MARGIN / IF Q2-1 OPEN
        if var['t2'] == 1 and var['s3'] == 1:
            if np.less(abs(var['vt2'] - var['vs3']), delta['V']).all():
                print(Fore.GREEN + 'SIED3 is ON')
            else:
                print(Fore.RED + 'SIED3 is ON - vt2: ' +
                      str(var['vt2']) + ', vs3: ' + str(var['vs3']))
        # Q3,Q3-1 = CLOSED -> TIED4 - SIED4 < V MARGIN / IF Q2-1 OPEN
        if var['t2'] == 1 and var['s4'] == 1:
            if np.less(abs(var['vt2'] - var['vs4']), delta['V']).all():
                print(Fore.GREEN + 'SIED4 is ON')
            else:
                print(Fore.RED + 'SIED4 is ON - vt2: ' +
                      str(var['vt2']) + ', vs4: ' + str(var['vs4']))

		# -----------------------------

        ####### NEED TO DO FOR Q1A, Q1 AND Q1-3 #######
		# ---------------------------------------------------------
		# Generation, where the (TIED1) - (GIED1 + GIED2) <= Voltage delta
		# 3 switches involved. (Q1A, Q1, Q1-3) 3^2 = 8cases?


		# ---------------------------------------------------------
        # TODO:I sw OFF
        # I sw OFF

        # Q2B = OPEN -> MIED1 < I MARGIN
        if var['m1'] == 0:
            if np.less(abs(var['im1']), delta['I']).all():
                print(Fore.GREEN + 'MIED1 is OFF')
            else:
                print(Fore.RED + 'MIED1 is OFF - im1: ' + str(var['im1']))
        # Q2C = OPEN -> MIED2 < I MARGIN
        if var['m2'] == 0:
            if np.less(abs(var['im2']), delta['I']).all():
                print(Fore.GREEN + 'MIED2 is OFF')
            else:
                print(Fore.RED + 'MIED2 is OFF - im2: ' + str(var['im2']))
        # Q2-1 = OPEN -> TIED4 < I MARGIN
        if var['t4'] == 0:
            if np.less(abs(var['it4']), delta['I']).all():
                print(Fore.GREEN + 'TIED4 is OFF')
            else:
                print(Fore.RED + 'TIED4 is OFF - it4: ' + str(var['it4']))
        # Q3-4 = OPEN -> SIED1 < I MARGIN
        if var['s1'] == 0:
            if np.less(abs(var['is1']), delta['I']).all():
                print(Fore.GREEN + 'SIED1 is OFF: I')
            else:
                print(Fore.RED + 'SIED1 is OFF - is1: ' + str(var['is1']))
        # Q3-3 = OPEN -> SIED2 < I MARGIN
        if var['s2'] == 0:
            if np.less(abs(var['is2']), delta['I']).all():
                print(Fore.GREEN + 'SIED2 is OFF: I')
            else:
                print(Fore.RED + 'SIED2 is OFF - is2: ' + str(var['is2']))
        # Q3-2 = OPEN -> SIED3 < I MARGIN
        if var['s3'] == 0:
            if np.less(abs(var['is3']), delta['I']).all():
                print(Fore.GREEN + 'SIED3 is OFF: I')
            else:
                print(Fore.RED + 'SIED3 is OFF - is3: ' + str(var['is3']))
        # Q3-1 = OPEN -> SIED4 < I MARGIN
        if var['s4'] == 0:
            if np.less(abs(var['is4']), delta['I']).all():
                print(Fore.GREEN + 'SIED4 is OFF: I')
            else:
                print(Fore.RED + 'SIED4 is OFF - is4: ' + str(var['is4']))

        # EditedByNicholas&TinKit
        # Q3 = OPEN -> TIED2 < I MARGIN
        if var['t2'] == 0:
            if np.less(abs(var['it2']), delta['I']).all():
                print(Fore.GREEN + 'TIED2 is OFF: I')
            else:
                print(Fore.RED + 'TIED2 is OFF - it2: ' + str(var['it2']))
        # Q1A = OPEN -> GIED2 < I MARGIN
        if var['g2'] == 0:
            if np.less(abs(var['ig2']), delta['I']).all():
                print(Fore.GREEN + 'GIED2 is OFF: I')
            else:
                print(Fore.RED + 'GIED2 is OFF - ig2: ' + str(var['ig2']))
        # Q1 = OPEN -> GIED1 < I MARGIN
        if var['g1'] == 0:
            if np.less(abs(var['ig1']), delta['I']).all():
                print(Fore.GREEN + 'GIED1 is OFF: I')
            else:
                print(Fore.RED + 'GIED1 is OFF - ig2: ' + str(var['ig2']))
        # Q1-3 = OPEN -> TIED1 < I MARGIN
        if var['t1'] == 0:
            if np.less(abs(var['it1']), delta['I']).all():
                print(Fore.GREEN + 'TIED1 is OFF: I')
            else:
                print(Fore.RED + 'TIED1 is OFF - it1: ' + str(var['it1']))
        
        # I sw ON
        if True:
            # (Q2B*MIED1) + (Q2C*MIED2) - (Q2-1*TIED4) < I MARGIN
            if np.less(abs(var['m1']*var['im1'] + var['m2']*var['im2'] - var['t4']*var['it4']), delta['I']).all():
                print(Fore.GREEN + 'MicroGrid-Transmission: Current')
            else:
                print(Fore.RED + 'MicroGrid-Transmission: Current - im1: ' +
                      str(var['im1']) + ', im2: ' + str(var['im2']) + ', it4: ' + str(var['it4']))
            # (Q2-1*TIED4) - (Q3-4*SIED1) - (Q3-3*SIED2) - (Q3-2*SIED3) - (Q3-1*SIED4) < I MARGIN / IF Q3 IS OPEN
            if np.less(abs(var['t4']*var['it4'] - var['s1']*var['is1'] - var['s2']*var['is2'] - var['s3']*var['is3'] - var['s4']*var['is4']), delta['I']).all():
                print(Fore.GREEN + 'Transmission-SmartHome: Current1')
            else:
                print(Fore.RED + 'Transmission-SmartHome: Current - it4: ' + str(var['it4']) + ', is1: ' + str(
                    var['is1']) + ', is2: ' + str(var['is2']) + ', is3: ' + str(var['is3']) + ', is4: ' + str(var['is4']))

            # EditedByNicholas&TinKit
            # (Q3*TIED2) - (Q3-4*SIED1) - (Q3-3*SIED2) - (Q3-2*SIED3) - (Q3-1*SIED4) < I MARGIN / IF Q2-1 IS OPEN
            if np.less(abs(var['t2']*var['it2'] - var['s1']*var['is1'] - var['s2']*var['is2'] - var['s3']*var['is3'] - var['s4']*var['is4']), delta['I']).all():
                print(Fore.GREEN + 'Transmission-SmartHome: Current2')
            else:
                print(Fore.RED + 'Transmission-SmartHome: Current - it2: ' + str(var['it2']) + ', is1: ' + str(
                    var['is1']) + ', is2: ' + str(var['is2']) + ', is3: ' + str(var['is3']) + ', is4: ' + str(var['is4']))
            # (Q1-3*TIED1) - (Q3*TIED2) < I MARGIN / IF Q3 IS CLOSED
            if np.less(abs(var['t1']*var['it1'] - var['t2']*var['it2']), delta['I']).all():
                print(Fore.GREEN + 'Transmission-SmartHome: Current')
            else:
                print(Fore.RED + 'Transmission-SmartHome: Current - it1: ' +
                      str(var['it1']) + ', it2: ' + str(var['it2']))

        ####### NEED TO DO FOR Q1A, Q1 AND Q1-3 #######
        # TODO:P sw OFF
        # P sw OFF

        # Q2B OPEN
        if var['m1'] == 0:
            # MIED1 - APPPARENT < P MARGIN
            if np.less(abs(var['papm1']), delta['P']).all():
                print(Fore.GREEN + 'MIED1 is OFF: P Apparent')
            else:
                print(Fore.RED + 'MIED1 is OFF - papm1: ' + str(var['papm1']))
            # MIED1 - REACTIVE < P MARGIN
            if np.less(abs(var['prcm1']), delta['P']).all():
                print(Fore.GREEN + 'MIED1 is OFF: P Reactive')
            else:
                print(Fore.RED + 'MIED1 is OFF - prcm1: ' + str(var['prcm1']))
            # MIED1 - REAL < P MARGIN
            if np.less(abs(var['prlm1']), delta['P']).all():
                print(Fore.GREEN + 'MIED1 is OFF: P Real')
            else:
                print(Fore.RED + 'MIED1 is OFF - prlm1: ' + str(var['prlm1']))
        # Q2C OPEN
        if var['m2'] == 0:
            # MIED2 - APPARENT < P MARGIN
            if np.less(abs(var['papm2']), delta['P']).all():
                print(Fore.GREEN + 'MIED2 is OFF: P Apparent')
            else:
                print(Fore.RED + 'MIED2 is OFF - papm2: ' + str(var['papm2']))
            # MIED2 - REACTIVE < P MARGIN
            if np.less(abs(var['prcm2']), delta['P']).all():
                print(Fore.GREEN + 'MIED2 is OFF: P Reactive')
            else:
                print(Fore.RED + 'MIED2 is OFF - prcm2: ' + str(var['prcm2']))
            # MIED2 - REAL < P MARGIN
            if np.less(abs(var['prlm2']), delta['P']).all():
                print(Fore.GREEN + 'MIED2 is OFF: P Real')
            else:
                print(Fore.RED + 'MIED2 is OFF - prlm2: ' + str(var['prlm2']))
        # Q2-1 OPEN
        if var['t4'] == 0:
            # TIED1 - APPARENT < P MARGIN
            if np.less(abs(var['papt4']), delta['P']).all():
                print(Fore.GREEN + 'TIED4 is OFF: P Apparent')
            else:
                print(Fore.RED + 'TIED4 is OFF - papt4: ' + str(var['papt4']))
            # TIED1 - REACTIVE < P MARGIN
            if np.less(abs(var['prct4']), delta['P']).all():
                print(Fore.GREEN + 'TIED4 is OFF: P Reactive')
            else:
                print(Fore.RED + 'TIED4 is OFF - prct4: ' + str(var['prct4']))
            # TIED1 - REAL < P MARGIN
            if np.less(abs(var['prlt4']), delta['P']).all():
                print(Fore.GREEN + 'TIED4 is OFF: P Real')
            else:
                print(Fore.RED + 'TIED4 is OFF - prlt4: ' + str(var['prlt4']))
        # Q3-4 OPEN
        if var['s1'] == 0:
            # SIED1 - APPARENT < P MARGIN
            if np.less(abs(var['paps1']), delta['P']).all():
                print(Fore.GREEN + 'SIED1 is OFF: P Apparent')
            else:
                print(Fore.RED + 'SIED1 is OFF - paps1: ' + str(var['paps1']))
            # SIED1 - REACTIVE < P MARGIN
            if np.less(abs(var['prcs1']), delta['P']).all():
                print(Fore.GREEN + 'SIED1 is OFF: P Reactive')
            else:
                print(Fore.RED + 'SIED1 is OFF - prcs1: ' + str(var['prcs1']))
            # SIED1 - REAL < P MARGIN
            if np.less(abs(var['prls1']), delta['P']).all():
                print(Fore.GREEN + 'SIED1 is OFF: P Real')
            else:
                print(Fore.RED + 'SIED1 is OFF - prls1: ' + str(var['prls1']))
        # Q3-3 OPEN
        if var['s2'] == 0:
            # SIED2 - APPARENT < P MARGIN
            if np.less(abs(var['paps2']), delta['P']).all():
                print(Fore.GREEN + 'SIED2 is OFF: P Apparent')
            else:
                print(Fore.RED + 'SIED2 is OFF - paps2: ' + str(var['paps2']))
            # SIED2 - REACTIVE < P MARGIN
            if np.less(abs(var['prcs2']), delta['P']).all():
                print(Fore.GREEN + 'SIED2 is OFF: P Reactive')
            else:
                print(Fore.RED + 'SIED2 is OFF - prcs2: ' + str(var['prcs2']))
            # SIED2 - REAL < P MARGIN
            if np.less(abs(var['prls2']), delta['P']).all():
                print(Fore.GREEN + 'SIED2 is OFF: P Real')
            else:
                print(Fore.RED + 'SIED2 is OFF - prls2: ' + str(var['prls2']))
        # Q3-2 OPEN
        if var['s3'] == 0:
            # SIED3 - APPARENT < P MARGIN
            if np.less(abs(var['paps3']), delta['P']).all():
                print(Fore.GREEN + 'SIED3 is OFF: P Apparent')
            else:
                print(Fore.RED + 'SIED3 is OFF - paps3: ' + str(var['paps3']))
            # SIED3 - REACTIVE < P MARGIN
            if np.less(abs(var['prcs3']), delta['P']).all():
                print(Fore.GREEN + 'SIED3 is OFF: P Reactive')
            else:
                print(Fore.RED + 'TIED4 is OFF - prcs3: ' + str(var['prcs3']))
            # SIED3 - REAL < P MARGIN
            if np.less(abs(var['prls3']), delta['P']).all():
                print(Fore.GREEN + 'SIED3 is OFF: P Real')
            else:
                print(Fore.RED + 'TIED4 is OFF - prls3: ' + str(var['prls3']))
        # Q3-1 OPEN
        if var['s4'] == 0:
            # SIED4 - APPARENT < P MARGIN
            if np.less(abs(var['paps4']), delta['I']).all():
                print(Fore.GREEN + 'SIED4 is OFF: P Apparent')
            else:
                print(Fore.RED + 'SIED4 is OFF - paps4: ' + str(var['paps4']))
            # SIED4 - REACTIVE < P MARGIN
            if np.less(abs(var['prcs4']), delta['I']).all():
                print(Fore.GREEN + 'SIED4 is OFF: P Reactive')
            else:
                print(Fore.RED + 'TIED4 is OFF - prcs4: ' + str(var['prcs4']))
            # SIED4 - REAL < P MARGIN
            if np.less(abs(var['prls4']), delta['I']).all():
                print(Fore.GREEN + 'SIED4 is OFF: P Real')
            else:
                print(Fore.RED + 'TIED4 is OFF - prls4: ' + str(var['prls4']))

        # EditedByNicholas&TinKit
        # Q3 OPEN
        if var['t2'] == 0:
            # TIED2 - APPARENT < P MARGIN
            if np.less(abs(var['papt2']), delta['P']).all():
                print(Fore.GREEN + 'TIED2 is OFF: P Apparent')
            else:
                print(Fore.RED + 'TIED2 is OFF - papt2: ' + str(var['papt2']))
            # TIED2 - REACTIVE < P MARGIN
            if np.less(abs(var['prct2']), delta['P']).all():
                print(Fore.GREEN + 'TIED2 is OFF: P Reactive')
            else:
                print(Fore.RED + 'TIED2 is OFF - prct2: ' + str(var['prct2']))
            # TIED2 - REAL < P MARGIN
            if np.less(abs(var['prlt2']), delta['P']).all():
                print(Fore.GREEN + 'TIED2 is OFF: P Real')
            else:
                print(Fore.RED + 'TIED2 is OFF - prlt2: ' + str(var['prlt2']))

        # Q1-A OPEN
        if var['g2'] == 0:
            # GIED2 - APPARENT < P MARGIN
            if np.less(abs(var['papg2']), delta['P']).all():
                print(Fore.GREEN + 'GIED2 is OFF: P Apparent')
            else:
                print(Fore.RED + 'GIED2 is OFF - papg2: ' + str(var['papg2']))
            # GIED2 - REACTIVE < P MARGIN
            if np.less(abs(var['prcg2']), delta['P']).all():
                print(Fore.GREEN + 'GIED2 is OFF: P Reactive')
            else:
                print(Fore.RED + 'GIED2 is OFF - prcg2: ' + str(var['prcg2']))
            # GIED2 - REAL < P MARGIN
            if np.less(abs(var['prlg2']), delta['P']).all():
                print(Fore.GREEN + 'GIED2 is OFF: P Real')
            else:
                print(Fore.RED + 'GIED2 is OFF - prlg2: ' + str(var['prlg2']))

        # Q1 OPEN
        if var['g1'] == 0:
            # GIED1 - APPARENT < P MARGIN
            if np.less(abs(var['papg1']), delta['P']).all():
                print(Fore.GREEN + 'GIED1 is OFF: P Apparent')
            else:
                print(Fore.RED + 'GIED1 is OFF - papg1: ' + str(var['papg1']))
            # GIED1 - REACTIVE < P MARGIN
            if np.less(abs(var['prcg1']), delta['P']).all():
                print(Fore.GREEN + 'GIED1 is OFF: P Reactive')
            else:
                print(Fore.RED + 'GIED1 is OFF - prcg1: ' + str(var['prcg1']))
            # GIED1 - REAL < P MARGIN
            if np.less(abs(var['prlg1']), delta['P']).all():
                print(Fore.GREEN + 'GIED1 is OFF: P Real')
            else:
                print(Fore.RED + 'GIED1 is OFF - prlg1: ' + str(var['prlg1']))

        # Q1-3 OPEN
        if var['t1'] == 0:
            # TIED1 - APPARENT < P MARGIN
            if np.less(abs(var['papt1']), delta['P']).all():
                print(Fore.GREEN + 'TIED1 is OFF: P Apparent')
            else:
                print(Fore.RED + 'TIED1 is OFF - papt1: ' + str(var['papt1']))
            # TIED1 - REACTIVE < P MARGIN
            if np.less(abs(var['prct1']), delta['P']).all():
                print(Fore.GREEN + 'TIED1 is OFF: P Reactive')
            else:
                print(Fore.RED + 'TIED1 is OFF - prct1: ' + str(var['prct1']))
            # TIED1 - REAL < P MARGIN
            if np.less(abs(var['prlt1']), delta['P']).all():
                print(Fore.GREEN + 'TIED1 is OFF: P Real')
            else:
                print(Fore.RED + 'TIED1 is OFF - prlt1: ' + str(var['prlt1']))

        # P sw ON
        if True:
            # (Q2B*MIED1-APPARENT) + (Q2C*MIED2-APPARENT) - (Q2-1*TIED4-APPARENT) < P MARGIN
            if np.less(abs(var['m1']*var['papm1'] + var['m2']*var['papm2'] - var['t4']*var['papt4']), delta['P']).all():
                print(Fore.GREEN + 'MicroGrid-Transmission: Power Apparent')
            else:
                print(Fore.RED + 'MicroGrid-Transmission: Power - papm1: ' + str(
                    var['papm1']) + ', papm2: ' + str(var['papm2']) + ', papt4: ' + str(var['papt4']))
            # (Q2B*MIED1-REACTIVE) + (Q2C*MIED2-REACTIVE) - (Q2-1*TIED4-REACTIVE) < P MARGIN
            if np.less(abs(var['m1']*var['prcm1'] + var['m2']*var['prcm2'] - var['t4']*var['prct4']), delta['P']).all():
                print(Fore.GREEN + 'MicroGrid-Transmission: Power Reactive')
            else:
                print(Fore.RED + 'MicroGrid-Transmission: Power - prcm1: ' + str(
                    var['prcm1']) + ', prcm2: ' + str(var['prcm2']) + ', prct4: ' + str(var['prct4']))
            # (Q2B*MIED1-REAL) +  (Q2C*MIED2-REAL) - (Q2-1*TIED4-REAL) < P MARGIN
            if np.less(abs(var['m1']*var['prlm1'] + var['m2']*var['prlm2'] - var['t4']*var['prlt4']), delta['P']).all():
                print(Fore.GREEN + 'MicroGrid-Transmission: Power Real')
            else:
                print(Fore.RED + 'MicroGrid-Transmission: Power - prlm1: ' + str(
                    var['prlm1']) + ', prlm2: ' + str(var['prlm2']) + ', prlt4: ' + str(var['prlt4']))
            # (Q2-1*TIED4-APPARENT) - (Q3-4*SIED1-APPARENT) - (Q3-3*SIED2-APPARENT) - (Q3-2*SIED3-APPARENT) - (Q3-1*SIED4-APPARENT) < P MARGIN  /  IF Q3 OPEN
            if np.less(abs(var['t4']*var['papt4'] - var['s1']*var['paps1'] - var['s2']*var['paps2'] - var['s3']*var['paps3'] - var['s4']*var['paps4']), delta['P']).all():
                print(Fore.GREEN + 'Transmission-SmartHome: Power Apparent')
            else:
                print(Fore.RED + 'Transmission-SmartHome: Power - papt4: ' + str(var['papt4']) + ', paps1: ' + str(
                    var['paps1']) + ', paps2: ' + str(var['paps2']) + ', paps3: ' + str(var['paps3']) + ', paps4: ' + str(var['paps4']))
            # (Q2-1*TIED4-REACTIVE) - (Q3-4*SIED1-REACTIVE) - (Q3-3*SIED2-REACTIVE) - (Q3-2*SIED3-REACTIVE) - (Q3-1*SIED4-REACTIVE) < P MARGIN  /  IF Q3 OPEN
            if np.less(abs(var['t4']*var['prct4'] - var['s1']*var['prcs1'] - var['s2']*var['prcs2'] - var['s3']*var['prcs3'] - var['s4']*var['prcs4']), delta['P']).all():
                print(Fore.GREEN + 'Transmission-SmartHome: Power Reactive')
            else:
                print(Fore.RED + 'Transmission-SmartHome: Power - prct4: ' + str(var['prct4']) + ', prcs1: ' + str(
                    var['prcs1']) + ', prcs2: ' + str(var['prcs2']) + ', prcs3: ' + str(var['prcs3']) + ', prcs4: ' + str(var['prcs4']))
            # (Q2-1*TIED4-REAL) - (Q3-4*SIED1-REAL) - (Q3-3*SIED2-REAL) - (Q3-2*SIED3-REAL) - (Q3-1*SIED4-REAL) < P MARGIN  /  IF Q3 OPEN
            if np.less(abs(var['t4']*var['prlt4'] - var['s1']*var['prls1'] - var['s2']*var['prls2'] - var['s3']*var['prls3'] - var['s4']*var['prls4']), delta['P']).all():
                print(Fore.GREEN + 'Transmission-SmartHome: Power Real')
            else:
                print(Fore.RED + 'Transmission-SmartHome: Power - prlt4: ' + str(var['prlt4']) + ', prls1: ' + str(
                    var['prls1']) + ', prls2: ' + str(var['prls2']) + ', prls3: ' + str(var['prls3']) + ', prls4: ' + str(var['prls4']))

            # EditedByNicholas&TinKit
            # (Q3*TIED2-APPARENT) - (Q3-4*SIED1-APPARENT) - (Q3-3*SIED2-APPARENT) - (Q3-2*SIED3-APPARENT) - (Q3-1*SIED4-APPARENT) < P MARGIN  /  IF Q2-1 OPEN
            if np.less(abs(var['t2']*var['papt2'] - var['s1']*var['paps1'] - var['s2']*var['paps2'] - var['s3']*var['paps3'] - var['s4']*var['paps4']), delta['P']).all():
                print(Fore.GREEN + 'Transmission-SmartHome: Power Apparent')
            else:
                print(Fore.RED + 'Transmission-SmartHome: Power - papt2: ' + str(var['papt2']) + ', paps1: ' + str(
                    var['paps1']) + ', paps2: ' + str(var['paps2']) + ', paps3: ' + str(var['paps3']) + ', paps4: ' + str(var['paps4']))
            # (Q3*TIED2-REACTIVE) - (Q3-4*SIED1-REACTIVE) - (Q3-3*SIED2-REACTIVE) - (Q3-2*SIED3-REACTIVE) - (Q3-1*SIED4-REACTIVE) < P MARGIN  /  IF Q2-1 OPEN
            if np.less(abs(var['t2']*var['prct2'] - var['s1']*var['prcs1'] - var['s2']*var['prcs2'] - var['s3']*var['prcs3'] - var['s4']*var['prcs4']), delta['P']).all():
                print(Fore.GREEN + 'Transmission-SmartHome: Power Reactive')
            else:
                print(Fore.RED + 'Transmission-SmartHome: Power - prct2: ' + str(var['prct2']) + ', prcs1: ' + str(
                    var['prcs1']) + ', prcs2: ' + str(var['prcs2']) + ', prcs3: ' + str(var['prcs3']) + ', prcs4: ' + str(var['prcs4']))
            # (Q3*TIED2-REAL) - (Q3-4*SIED1-REAL) - (Q3-3*SIED2-REAL) - (Q3-2*SIED3-REAL) - (Q3-1*SIED4-REAL) < P MARGIN  /  IF Q2-1 OPEN
            if np.less(abs(var['t2']*var['prlt2'] - var['s1']*var['prls1'] - var['s2']*var['prls2'] - var['s3']*var['prls3'] - var['s4']*var['prls4']), delta['P']).all():
                print(Fore.GREEN + 'Transmission-SmartHome: Power Real')
            else:
                print(Fore.RED + 'Transmission-SmartHome: Power - prlt2: ' + str(var['prlt2']) + ', prls1: ' + str(
                    var['prls1']) + ', prls2: ' + str(var['prls2']) + ', prls3: ' + str(var['prls3']) + ', prls4: ' + str(var['prls4']))

            # (Q1-3*TIED1-APPARENT) - (Q3*TIED2-APPARENT) < P MARGIN
            if np.less(abs(var['t1']*var['papt1'] - var['t2']*var['papt2']), delta['P']).all():
                print(Fore.GREEN + 'Transmission - SmartHome: Power Apparent')
            else:
                print(Fore.RED + 'Transmission - SmartHome: Power - papt1: ' +
                      str(var['papt1']) + ', papt2: ' + str(var['papt2']))
            # (Q1-3*TIED1-REACTIVE) - (Q3*TIED2-REACTIVE) < P MARGIN
            if np.less(abs(var['t1']*var['prct1'] - var['t2']*var['prct2']), delta['P']).all():
                print(Fore.GREEN + 'Transmission - SmartHome: Power Reactive')
            else:
                print(Fore.RED + 'Transmission - SmartHome: Power - prct1: ' +
                      str(var['prct1']) + ', prct2: ' + str(var['prct2']))
            # (Q1-3*TIED1-REAL) - (Q3*TIED2-REAL) < P MARGIN
            if np.less(abs(var['t1']*var['prlt1'] - var['t2']*var['prlt2']), delta['P']).all():
                print(Fore.GREEN + 'Transmission - SmartHome: Power Real')
            else:
                print(Fore.RED + 'Transmission - SmartHome: Power - prlt1: ' +
                      str(var['prlt1']) + ', prlt2: ' + str(var['prlt2']))

            ####### NEED TO DO FOR Q1A, Q1 AND Q1-3 #######

        time.sleep(1)
        print
        if _DEB == 'printall':
            print_arr(var)
        if _ENV == '1line':
            endc = False

except KeyboardInterrupt:
    pass
