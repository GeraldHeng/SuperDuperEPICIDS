# ------------------------- COMMON -------------------------------------
# MARGINS VALUES
# CURRENT_MARGIN = 0.5  # 0.45 3
# BASED ON 5% of all current values.
CURRENT_MARGIN = 2.881219719237589
VOLTAGE_MARGIN = 4.5  # 10% 245 / 420
POWER_MARGIN = 175  # 150 (2150)

# TYPE
SWITCH = 'switch'
IED = 'ied'

# Data path for different scenario.
DATA = '../data/'
DATA_LIST = {'Real EPIC': [
    {'name': 'scenario 1', 'path': DATA +
        'real_epic/Scenario_1/EpicLog_Scenario 1_19_Oct_2018_14_44.csv',
        'type': 're_csv'},
    {'name': 'scenario 2', 'path': DATA +
        'real_epic/Scenario_2/EpicLog_Scenario 2_19_Oct_2018_14_56.csv',
        'type': 're_csv'},
    {'name': 'scenario 3', 'path': DATA +
        'real_epic/Scenario_3/EpicLog_Scenario 3_19_Oct_2018_15_02.csv',
        'type': 're_csv'},
    {'name': 'scenario 4', 'path': DATA +
        'real_epic/Scenario_4/EpicLog_Scenario 4_19_Oct_2018_15_23.csv',
        'type': 're_csv'},
    {'name': 'scenario 5', 'path': DATA +
        'real_epic/Scenario_5/EpicLog_Scenario 5_19_Oct_2018_15_45.csv',
        'type': 're_csv'},
    {'name': 'scenario 6', 'path': DATA +
        'real_epic/Scenario_6/EpicLog_Scenario 6_19_Oct_2018_16_06.csv',
        'type': 're_csv'},
    {'name': 'scenario 7', 'path': DATA +
        'real_epic/Scenario_7/EpicLog_Scenario 7_07_Nov_2018_14_40.csv',
        'type': 're_csv'},
    {'name': 'scenario 8', 'path': DATA +
        'real_epic/Scenario_8/EpicLog_Scenario 8_07_Nov_2018_14_57.csv',
        'type': 're_csv'},
],
    #     'Digital Twin': [
    #     {'name': 'MQTT txt file', 'path': DATA +
    #      'mqttlog.txt',
    #      'type': 'dt_mqtt_txt'}
    # ]
}
# SCENARIO_1_NAME = 'scenario 1'
# SCENARIO_1_PATH = DATA + 'Scenario_1/EpicLog_Scenario 1_19_Oct_2018_14_44.csv'
# SCENARIO_2_PATH = DATA + 'Scenario_2/EpicLog_Scenario 2_19_Oct_2018_14_56.csv'
# SCENARIO_2_NAME = 'scenario 2'
# SCENARIO_3_PATH = DATA + 'Scenario_3/EpicLog_Scenario 3_19_Oct_2018_15_02.csv'
# SCENARIO_3_NAME = 'scenario 3'
# SCENARIO_4_PATH = DATA + 'Scenario_4/EpicLog_Scenario 4_19_Oct_2018_15_23.csv'
# SCENARIO_4_NAME = 'scenario 4'
# SCENARIO_5_PATH = DATA + 'Scenario_5/EpicLog_Scenario 5_19_Oct_2018_15_45.csv'
# SCENARIO_5_NAME = 'scenario 5'
# SCENARIO_6_PATH = DATA + 'Scenario_6/EpicLog_Scenario 6_19_Oct_2018_16_06.csv'
# SCENARIO_6_NAME = 'scenario 6'
# SCENARIO_7_PATH = DATA + 'Scenario_7/EpicLog_Scenario 7_07_Nov_2018_14_40.csv'
# SCENARIO_7_NAME = 'scenario 7'
# SCENARIO_8_PATH = DATA + 'Scenario_8/EpicLog_Scenario 8_07_Nov_2018_14_57.csv'
# SCENARIO_8_NAME = 'scenario 8'

# ------------------------- IED -------------------------------------
# IED VALUES
FERQUENCY = 'Measurement.Frequency'
CURRENT_L1 = 'Measurement.L1_Current'
CURRENT_L2 = 'Measurement.L2_Current'
CURRENT_L3 = 'Measurement.L3_Current'
POWER_FACTOR = 'Measurement.Power_Factor'
POWER_APPARENT = 'Measurement.Apparent'
POWER_REACTIVE = 'Measurement.Reactive'
POWER_REAL = 'Measurement.Real'
VOLTAGE_V1 = 'Measurement.V1'
VOLTAGE_V2 = 'Measurement.V2'
VOLTAGE_V3 = 'Measurement.V3'
VOLTAGE_VL1_L2 = 'Measurement.VL1_L2'
VOLTAGE_VL2_L3 = 'Measurement.VL2_L3'
VOLTAGE_VL3_VL1 = 'Measurement.VL3_VL1'
ACTIVE_ENERGY_KWH = 'Active_Energy_KWh'
POWER_FRQUENCY = 'Power_Frequency'

# IED VALUES TO BE USED.
IED_VALUES = [
    FERQUENCY, CURRENT_L1,
    CURRENT_L2, CURRENT_L3,
    POWER_FACTOR, POWER_APPARENT,
    POWER_REACTIVE, POWER_REAL,
    VOLTAGE_V1, VOLTAGE_V2,
    VOLTAGE_V3, VOLTAGE_VL1_L2,
    VOLTAGE_VL2_L3, VOLTAGE_VL3_VL1
]

# ------------------------- SWITCH -------------------------------------
# SWITCH VALUES
M_CLOSE = 'MODE_CLOSE'
M_OPEN = 'MODE_OPEN'
M_STATUS = 'MODE_STATUS'
M_SYNC = 'MODE_SYNC'
SYNCHECK = '_Syncheck'
STATUS = 'STATUS'
S_CLOSE = 'STATUS_CLOSE'
S_OPEN = 'STATUS_OPEN'
TRIP = 'TRIP'

# SWITCH VALUES TO BE USED.
SWITCH_VALUES = [
    STATUS, S_CLOSE, S_OPEN
]

# ------------------------- VALUES SLD -------------------------------------
# Components and items of SLD to be defined here.
VALUES = {
    'MicroGrid': {
        'MIED1': {'type': IED},
        'MIED2': {'type': IED},
        'Q2': {'type': SWITCH},
        'Q2A': {'type': SWITCH},
        'Q2B': {'type': SWITCH, 'connected_to': 'MIED1'},
        'Q2C': {'type': SWITCH, 'connected_to': 'MIED2'}
    },
    'SmartHome': {
        'SIED1': {'type': IED},
        'SIED2': {'type': IED},
        'SIED3': {'type': IED},
        'SIED4': {'type': IED},
        'Q3-1': {'type': SWITCH, 'connected_to': 'SIED4'},
        'Q3-2': {'type': SWITCH, 'connected_to': 'SIED3'},
        'Q3-3': {'type': SWITCH, 'connected_to': 'SIED2'},
        'Q3-4': {'type': SWITCH, 'connected_to': 'SIED1'}
    },
    'Generation': {
        'GIED1': {'type': IED},
        'GIED2': {'type': IED},
        'Q1': {'type': SWITCH, 'connected_to': 'GIED1'},
        'Q1A': {'type': SWITCH, 'connected_to': 'GIED2'},
        'Q1-1': {'type': SWITCH},
        'Q1-2': {'type': SWITCH},
        # 'Q1-4': {'type': SWITCH},
        # 'Q1-5': {'type': SWITCH},
    },
    'Transmission': {
        'TIED1': {'type': IED},
        'TIED4': {'type': IED},
        'TIED2': {'type': IED},
        'Q3': {'type': SWITCH, 'connected_to': 'TIED2'},
        'Q1-3': {'type': SWITCH, 'connected_to': 'TIED1'},
        'Q2-1': {'type': SWITCH, 'connected_to': 'TIED4'},
    }
}

DT_VALUES = {
    'MicroGrid': {
        # 'MIED1': {'type': IED},
        # 'MIED2': {'type': IED},
        'M1Meter': {'type': IED},
        'M2Meter': {'type': IED},
        'PVMeter': {'type': IED},
        'Q2': {'type': SWITCH},
        'Q2A': {'type': SWITCH},
        'Q2B': {'type': SWITCH, 'connected_to': 'MIED1'},
        'Q2C': {'type': SWITCH, 'connected_to': 'MIED2'}
    },
    'SmartHome': {
        'S2Meter': {'type': IED},
        'S3Meter': {'type': IED},
        'S4Meter': {'type': IED},
        'Q4_1': {'type': SWITCH, 'connected_to': 'S4Meter'},
        'Q4_2': {'type': SWITCH, 'connected_to': 'S3Meter'},
        'Q4_3': {'type': SWITCH, 'connected_to': 'S2Meter'},
        'Q4_4': {'type': SWITCH}
    },
    'Generation': {
        'G3Meter': {'type': IED},
        # 'Q1': {'type': SWITCH, 'connected_to': 'GIED1'},
        # 'Q1A': {'type': SWITCH, 'connected_to': 'GIED2'},
        # 'Q1_1': {'type': SWITCH},
        # 'Q1_2': {'type': SWITCH},
        # 'Q1-4': {'type': SWITCH},
        # 'Q1-5': {'type': SWITCH},
    },
    'Transmission': {
        'T1Meter': {'type': IED},
        'T2Meter': {'type': IED},
        'Q31': {'type': SWITCH, 'connected_to': 'TIED2'},
        'Q32_A': {'type': SWITCH, 'connected_to': 'TIED1'},
        'Q32_B': {'type': SWITCH, 'connected_to': 'TIED4'},
    }
}


# ------------------------- USELESS -------------------------------------
# VSD
ACTUAL_SPEED = 'ActualSpeed'
VSD_CURRENT = 'Current'
E_STOP = 'E_Stop'
FAULT = 'Fault'
READY = 'Ready'
RESET = 'Reset'
START = 'Start'
START_FLAG = 'Start_Flag'
STOP = 'Stop'
STOP_FLAG = 'Stop_Flag'
