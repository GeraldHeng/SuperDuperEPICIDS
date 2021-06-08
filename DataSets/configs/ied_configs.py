'''
This script contains the true values for each Meter.
'''

from random import uniform

MIED1 = {
    'MicroGrid.MIED1.Measurement.Apparent': uniform(1636.74,3091.58),
    'MicroGrid.MIED1.Measurement.Frequency': uniform(49.98,50.0101),
    'MicroGrid.MIED1.Measurement.L1_Current': uniform(3.19,5.42),
    'MicroGrid.MIED1.Measurement.L2_Current': uniform(1.53,3.65),
    'MicroGrid.MIED1.Measurement.L3_Current': uniform(1.89,4.32),
    'MicroGrid.MIED1.Measurement.Power_Factor': uniform(0.91,0.99),
    'MicroGrid.MIED1.Measurement.Reactive': uniform(-78.47,988.72),
    'MicroGrid.MIED1.Measurement.Real': uniform(1636,2825.55),
    'MicroGrid.MIED1.Measurement.V1': uniform(240.58,242.02),
    'MicroGrid.MIED1.Measurement.V2': uniform(242.40,243.54),
    'MicroGrid.MIED1.Measurement.V3': uniform(242.56,244.05),
    'MicroGrid.MIED1.Measurement.VL1_L2': uniform(417.27,419.62),
    'MicroGrid.MIED1.Measurement.VL2_L3': uniform(421.77,424.3),
    'MicroGrid.MIED1.Measurement.VL3_L1': uniform(417.80,419.95)
}


MIED2 = {
    'MicroGrid.MIED2.Measurement.Apparent': uniform(1696.786,2913.669),
    'MicroGrid.MIED2.Measurement.Frequency': uniform(49.981,50.090),
    'MicroGrid.MIED2.Measurement.L1_Current': uniform(3.245,5.0999),
    'MicroGrid.MIED2.Measurement.L2_Current': uniform(1.54999, 3.3249),
    'MicroGrid.MIED2.Measurement.L3_Current': uniform(1.9249,3.74999),
    'MicroGrid.MIED2.Measurement.Power_Factor': uniform(0.87999,0.9909),
    'MicroGrid.MIED2.Measurement.Reactive': uniform(260.2888,1340.8095),
    'MicroGrid.MIED2.Measurement.Real': uniform(1642.616,2664.886),
    'MicroGrid.MIED2.Measurement.V1': uniform(237.686,242.0619),
    'MicroGrid.MIED2.Measurement.V2': uniform(242.0732,243.989),
    'MicroGrid.MIED2.Measurement.V3': uniform(243.1899,244.782),
    'MicroGrid.MIED2.Measurement.VL1_L2': uniform(417.5012,420.19116),
    'MicroGrid.MIED2.Measurement.VL2_L3': uniform(421.655,424.145),
    'MicroGrid.MIED2.Measurement.VL3_L1': uniform(417.667,419.531)
}


def update_IED(node:object, dict:dict):
    '''
    Updates the Input Node Variables

    @Param Node $node
    @Param dict $dict
    '''
    # print(node.get_browse_name().to_string())

    if node.get_browse_name().to_string() == '2:MicroGrid.MIED1':
        dict['MicroGrid.MIED1.Measurement.Apparent'] = uniform(1636.74,3091.58)
        dict['MicroGrid.MIED1.Measurement.Frequency'] = uniform(49.98,50.0101)
        dict['MicroGrid.MIED1.Measurement.L1_Current'] = uniform(3.19,5.42)
        dict['MicroGrid.MIED1.Measurement.L2_Current'] = uniform(1.53,3.65)
        dict['MicroGrid.MIED1.Measurement.L3_Current'] = uniform(1.89,4.32)
        dict['MicroGrid.MIED1.Measurement.Power_Factor'] = uniform(0.91,0.99)
        dict['MicroGrid.MIED1.Measurement.Reactive'] = uniform(-78.47,988.72)
        dict['MicroGrid.MIED1.Measurement.Real'] = uniform(1636,2825.55)
        dict['MicroGrid.MIED1.Measurement.V1'] = uniform(240.58,242.02)
        dict['MicroGrid.MIED1.Measurement.V2'] = uniform(242.40,243.54)
        dict['MicroGrid.MIED1.Measurement.V3'] = uniform(242.56,244.05)
        dict['MicroGrid.MIED1.Measurement.VL1_L2'] = uniform(417.27,419.62)
        dict['MicroGrid.MIED1.Measurement.VL2_L3'] = uniform(421.77,424.3)
        dict['MicroGrid.MIED1.Measurement.VL3_VL1'] = uniform(417.80,419.95)

    elif node.get_browse_name().to_string() == '2:MicroGrid.MIED2':
        dict['MicroGrid.MIED2.Measurement.Apparent'] = uniform(1696.786,2913.669)
        dict['MicroGrid.MIED2.Measurement.Frequency'] = uniform(49.981,50.090)
        dict['MicroGrid.MIED2.Measurement.L1_Current'] = uniform(3.245,5.0999)
        dict['MicroGrid.MIED2.Measurement.L2_Current'] = uniform(1.54999, 3.3249)
        dict['MicroGrid.MIED2.Measurement.L3_Current'] = uniform(1.9249,3.74999)
        dict['MicroGrid.MIED2.Measurement.Power_Factor'] = uniform(0.87999,0.9909)
        dict['MicroGrid.MIED2.Measurement.Reactive'] = uniform(260.2888,1340.8095)
        dict['MicroGrid.MIED2.Measurement.Real'] = uniform(1642.616,2664.886)
        dict['MicroGrid.MIED2.Measurement.V1'] = uniform(237.686,242.0619)
        dict['MicroGrid.MIED2.Measurement.V2'] = uniform(242.0732,243.989)
        dict['MicroGrid.MIED2.Measurement.V3'] = uniform(243.1899,244.782)
        dict['MicroGrid.MIED2.Measurement.VL1_L2'] = uniform(417.5012,420.19116)
        dict['MicroGrid.MIED2.Measurement.VL2_L3'] =uniform(421.655,424.145)
        dict['MicroGrid.MIED2.Measurement.VL3_VL1'] = uniform(417.667,419.531)

    return dict
