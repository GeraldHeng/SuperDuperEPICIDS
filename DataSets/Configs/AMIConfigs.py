'''
This script contains the true values for each Meter.
'''

from random import uniform

MAMI1 = {
    'MicroGrid.MAMI1.Voltage_L1': uniform(236.4689,236.932),
    'MicroGrid.MAMI1.Voltage_L2': uniform(240.281,2408.8229),
    'MicroGrid.MAMI1.Voltage_L3': uniform(240.8229,241.5),
    'MicroGrid.MAMI1.Current_L1': uniform(3.75,4.67999),
    'MicroGrid.MAMI1.Current_L2': uniform(1.53999,2.96),
    'MicroGrid.MAMI1.Current_L3': uniform(1.83,3.52960),
    'MicroGrid.MAMI1.Active_Energy_KWh': uniform(60,60.6699),
    'MicroGrid.MAMI1.Power_Factor': uniform(0.9467,0.999),
    'MicroGrid.MAMI1.Power_Frequency': uniform(50.02,50.0499)
}

MAMI2 = {
    'MicroGrid.MAMI2.Voltage_L1': uniform(235.713,236.647),
    'MicroGrid.MAMI2.Voltage_L2': uniform(239.619,240.588),
    'MicroGrid.MAMI2.Voltage_L3': uniform(240.153,241.509),
    'MicroGrid.MAMI2.Current_L1': uniform(3.300,4.910),
    'MicroGrid.MAMI2.Current_L2': uniform(1.570,3.240),
    'MicroGrid.MAMI2.Current_L3': uniform(1.870,3.630),
    'MicroGrid.MAMI2.Active_Energy_KWh': uniform(640.700,641.380),
    'MicroGrid.MAMI2.Power_Factor': uniform(0.906,0.996),
    'MicroGrid.MAMI2.Power_Frequency': uniform(50.020,50.060)
}

MAMI3 = {
    'MicroGrid.MAMI3.Voltage_L1': uniform(235.474,236.615),
    'MicroGrid.MAMI3.Voltage_L2': uniform(239.565,240.592),
    'MicroGrid.MAMI3.Voltage_L3': uniform(240.072,241.344),
    'MicroGrid.MAMI3.Current_L1': uniform(0,0),
    'MicroGrid.MAMI3.Current_L2': uniform(0,0),
    'MicroGrid.MAMI3.Current_L3': uniform(0,0),
    'MicroGrid.MAMI3.Active_Energy_KWh': uniform(551.71,551.71),
    'MicroGrid.MAMI3.Power_Factor': uniform(1,1),
    'MicroGrid.MAMI3.Power_Frequency': uniform(50.020,50.070)
}

def update_AMI(node: object, dict: dict):
    '''
    Updates the appropriate AMI Meter Accordingly.

    @Param Node $sector
    @Param dict $dict
    '''


    if node.get_browse_name().to_string() == '2:MAMI1':
        dict['MicroGrid.MAMI1.Voltage_L1'] = uniform(236.4689,236.932)
        dict['MicroGrid.MAMI1.Voltage_L2'] = uniform(240.281,2408.8229)
        dict['MicroGrid.MAMI1.Voltage_L3'] = uniform(240.8229,241.5)
        dict['MicroGrid.MAMI1.Current_L1'] = uniform(3.75,4.67999)
        dict['MicroGrid.MAMI1.Current_L2'] = uniform(1.53999,2.96)
        dict['MicroGrid.MAMI1.Current_L3'] = uniform(1.83,3.52960)
        dict['MicroGrid.MAMI1.Active_Energy_KWh'] = uniform(60,60.6699)
        dict['MicroGrid.MAMI1.Power_Factor'] = uniform(0.9467,0.999)
        dict['MicroGrid.MAMI1.Power_Frequency'] = uniform(50.02,50.0499)

    elif node.get_browse_name().to_string() == '2:MAMI2':
        dict['MicroGrid.MAMI2.Voltage_L1'] = uniform(235.713,236.647)
        dict['MicroGrid.MAMI2.Voltage_L2'] = uniform(239.619,240.588)
        dict['MicroGrid.MAMI2.Voltage_L3'] = uniform(240.153,241.509)
        dict['MicroGrid.MAMI2.Current_L1'] = uniform(3.300,4.910)
        dict['MicroGrid.MAMI2.Current_L2'] = uniform(1.570,3.240)
        dict['MicroGrid.MAMI2.Current_L3'] = uniform(1.870,3.630)
        dict['MicroGrid.MAMI2.Active_Energy_KWh'] = uniform(551.71,551.71)
        dict['MicroGrid.MAMI2.Power_Factor'] = uniform(1,1)
        dict['MicroGrid.MAMI2.Power_Frequency'] = uniform(50.020,50.060)

    elif node.get_browse_name().to_string() == '2:MAMI3':
        dict['MicroGrid.MAMI3.Voltage_L1'] = uniform(235.474,236.615)
        dict['MicroGrid.MAMI3.Voltage_L2'] = uniform(239.565,240.592)
        dict['MicroGrid.MAMI3.Voltage_L3'] = uniform(240.072,241.344)
        dict['MicroGrid.MAMI3.Current_L1'] = uniform(0,0)
        dict['MicroGrid.MAMI3.Current_L2'] = uniform(0,0)
        dict['MicroGrid.MAMI3.Current_L3'] = uniform(0,0)
        dict['MicroGrid.MAMI3.Active_Energy_KWh'] = uniform(60,60.6699)
        dict['MicroGrid.MAMI3.Power_Factor'] = uniform(0.9467,0.999)
        dict['MicroGrid.MAMI3.Power_Frequency'] = uniform(50.020,50.070)

    return dict
