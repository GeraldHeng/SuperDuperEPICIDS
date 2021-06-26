import sys
import opcua
from random import randint
import constant


def setting_values(node: object, values: dict,):
    '''
    Set values for each individual variable of input Node

    @Param Node: $node
    @Param float: $values
    '''
    # Set Values for IED Meters
    if 'IED' in node.get_browse_name().to_string():
        if '2:MicroGrid.MIED' in node.get_browse_name().to_string():
            sector = 'MicroGrid'
            sectorLetter = 'M'
        elif '2:Generation.GIED' in node.get_browse_name().to_string():
            sector = 'Generation'
            sectorLetter = 'G'
        elif '2:SmartHome.SIED' in node.get_browse_name().to_string():
            sector = 'SmartHome'
            sectorLetter = 'S'
        elif '2:Transmission.TIED' in node.get_browse_name().to_string():
            sector = 'Transmission'
            sectorLetter = 'T'
        else:
            raise Exception('Not a Valid Browse Name' +
                            node.get_browse_name().to_string())

        try:
            for var in node.get_variables():
                # print(var.get_browse_name().to_string())
                # print('2:{}.{}IED{}.Measurement.Apparent'.format(
                #     sector, sectorLetter, node.get_browse_name().to_string()[-1]))

                # if var.get_browse_name().to_string() == '2:{}.{}IED{}.Measurement.Apparent'.format(sector, sectorLetter, node.get_browse_name().to_string()[-1]):
                if constant.POWER_APPARENT in var.get_browse_name().to_string() or \
                        constant.FERQUENCY in var.get_browse_name().to_string() or \
                        constant.CURRENT_L1 in var.get_browse_name().to_string() or \
                        constant.CURRENT_L2 in var.get_browse_name().to_string() or \
                        constant.CURRENT_L3 in var.get_browse_name().to_string() or \
                        constant.POWER_FACTOR in var.get_browse_name().to_string() or \
                        constant.POWER_REACTIVE in var.get_browse_name().to_string() or \
                        constant.POWER_REAL in var.get_browse_name().to_string() or \
                        constant.VOLTAGE_V1 in var.get_browse_name().to_string() or \
                        constant.VOLTAGE_V2 in var.get_browse_name().to_string() or \
                        constant.VOLTAGE_V3 in var.get_browse_name().to_string() or \
                        constant.VOLTAGE_VL1_L2 in var.get_browse_name().to_string() or \
                        constant.VOLTAGE_VL2_L3 in var.get_browse_name().to_string() or \
                        constant.VOLTAGE_VL3_VL1 in var.get_browse_name().to_string():

                    # var.set_value(float(values['{}.{}IED{}.Measurement.Apparent'.format(
                    #     sector, sectorLetter, node.get_browse_name().to_string()[-1])]))
                    var.set_value(
                        float(values[var.get_browse_name().to_string()[2:]]))

                # elif var.get_browse_name().to_string() == '2:{}.{}IED{}.Measurement.Frequency'.format(sector, sectorLetter, node.get_browse_name().to_string()[-1]):
                # elif constant.FERQUENCY in var.get_browse_name().to_string():
                #     var.set_value(float(values['{}.{}IED{}.Measurement.Frequency'.format(
                #         sector, sectorLetter, node.get_browse_name().to_string()[-1])]))

                # elif var.get_browse_name().to_string() == '2:{}.{}IED{}.Measurement.L1_Current'.format(sector, sectorLetter, node.get_browse_name().to_string()[-1]):
                # elif constant.CURRENT_L1 in var.get_browse_name().to_string():
                #     var.set_value(float(values['{}.{}IED{}.Measurement.L1_Current'.format(
                #         sector, sectorLetter, node.get_browse_name().to_string()[-1])]))

                # elif constant.CURRENT_L2 in var.get_browse_name().to_string():
                #     var.set_value(float(values['{}.{}IED{}.Measurement.L2_Current'.format(
                #         sector, sectorLetter, node.get_browse_name().to_string()[-1])]))

                # elif constant.CURRENT_L3 in var.get_browse_name().to_string():
                #     var.set_value(float(values['{}.{}IED{}.Measurement.L3_Current'.format(
                #         sector, sectorLetter, node.get_browse_name().to_string()[-1])]))

                # elif constant.POWER_FACTOR in var.get_browse_name().to_string():
                #     var.set_value(float(values['{}.{}IED{}.Measurement.Power_Factor'.format(
                #         sector, sectorLetter, node.get_browse_name().to_string()[-1])]))

                # elif constant.POWER_REACTIVE in var.get_browse_name().to_string():
                #     var.set_value(float(values['{}.{}IED{}.Measurement.Reactive'.format(
                #         sector, sectorLetter, node.get_browse_name().to_string()[-1])]))

                # elif constant.POWER_REAL in var.get_browse_name().to_string():
                #     var.set_value(float(values['{}.{}IED{}.Measurement.Real'.format(
                #         sector, sectorLetter, node.get_browse_name().to_string()[-1])]))

                # elif constant.VOLTAGE_V1 in var.get_browse_name().to_string():
                #     var.set_value(float(values['{}.{}IED{}.Measurement.V1'.format(
                #         sector, sectorLetter, node.get_browse_name().to_string()[-1])]))

                # elif constant.VOLTAGE_V2 in var.get_browse_name().to_string():
                #     var.set_value(float(values['{}.{}IED{}.Measurement.V2'.format(
                #         sector, sectorLetter, node.get_browse_name().to_string()[-1])]))

                # elif constant.VOLTAGE_V3 in var.get_browse_name().to_string():
                #     var.set_value(float(values['{}.{}IED{}.Measurement.V3'.format(
                #         sector, sectorLetter, node.get_browse_name().to_string()[-1])]))

                # elif constant.VOLTAGE_VL1_L2 in var.get_browse_name().to_string():
                #     var.set_value(float(values['{}.{}IED{}.Measurement.VL1_L2'.format(
                #         sector, sectorLetter, node.get_browse_name().to_string()[-1])]))

                # elif constant.VOLTAGE_VL2_L3 in var.get_browse_name().to_string():
                #     var.set_value(float(values['{}.{}IED{}.Measurement.VL2_L3'.format(
                #         sector, sectorLetter, node.get_browse_name().to_string()[-1])]))

                # elif constant.VOLTAGE_VL3_VL1 in var.get_browse_name().to_string():
                #     var.set_value(float(values['{}.{}IED{}.Measurement.VL3_VL1'.format(
                #         sector, sectorLetter, node.get_browse_name().to_string()[-1])]))

        except Exception as e:
            # e
            print(str(e) + ' is an error')

    # Set Values for AMI Meters
    elif 'AMI' in node.get_browse_name().to_string():
        if node.get_browse_name().to_string() == '2:MicroGrid.MAMI{}'.format(1):
            sector = 'MicroGrid'
            sectorLetter = 'M'
        elif node.get_browse_name().to_string() == '2:Generation.GAMI{}'.format(1):
            sector = 'Generation'
            sectorLetter = 'G'
        elif node.get_browse_name().to_string() == '2:SmartHome.SAMI{}'.format(1):
            sectorLetter = 'SmartHome'
            sectorLetter = 'S'
        elif node.get_browse_name().to_string() == '2:Transmission.TAMI{}'.format(1):
            sector = 'Transmission'
            sectorLetter = 'T'
        else:
            raise Exception('Not a Valid Browse Name')

        try:
            for var in node.get_variables():
                if var.get_browse_name().to_string() == '2:{}.{}AMI{}.Voltage_L1'.format(sector, sectorLetter, deviceNo):
                    var.set_value(values['{}.{}AMI{}.Voltage_L1'.format(
                        sector, sectorLetter, 1)])
                elif var.get_browse_name().to_string() == '2:{}.{}AMI{}.Voltage_L2'.format(sector, sectorLetter, deviceNo):
                    var.set_value(values['{}.{}AMI{}.Voltage_L2'.format(
                        sector, sectorLetter, 1)])
                elif var.get_browse_name().to_string() == '2:{}.{}AMI{}.Voltage_L3'.format(sector, sectorLetter, deviceNo):
                    var.set_value(values['{}.{}AMI{}.Voltage_L3'.format(
                        sector, sectorLetter, 1)])
                elif var.get_browse_name().to_string() == '2:{}.{}AMI{}.Current_L1'.format(sector, sectorLetter, deviceNo):
                    var.set_value(values['{}.{}AMI{}.Current_L1'.format(
                        sector, sectorLetter, 1)])
                elif var.get_browse_name().to_string() == '2:{}.{}AMI{}.Current_L2'.format(sector, sectorLetter, deviceNo):
                    var.set_value(values['{}.{}AMI{}.Current_L2'.format(
                        sector, sectorLetter, 1)])
                elif var.get_browse_name().to_string() == '2:{}.{}AMI{}.Current_L3'.format(sector, sectorLetter, deviceNo):
                    var.set_value(values['{}.{}AMI{}.Current_L3'.format(
                        sector, sectorLetter, 1)])
                elif var.get_browse_name().to_string() == '2:{}.{}AMI{}.Active_Energy_KWh'.format(sector, sectorLetter, deviceNo):
                    var.set_value(values['{}.{}AMI{}.Active_Energy_KWh'.format(
                        sector, sectorLetter, 1)])
                elif var.get_browse_name().to_string() == '2:{}.{}AMI{}.Power_Factor'.format(sector, sectorLetter, deviceNo):
                    var.set_value(values['{}.{}AMI{}.Power_Factor'.format(
                        sector, sectorLetter, 1)])
                elif var.get_browse_name().to_string() == '2:{}.{}AMI{}.Power_Frequency'.format(sector, sectorLetter, deviceNo):
                    var.set_value(values['{}.{}AMI{}.Power_Frequency'.format(
                        sector, sectorLetter, 1)])
        except Exception as e:
            print(e)
    else:
        try:
            for var in node.get_variables():
                # print(var.get_browse_name().to_string()[2:])

                if 'STATUS_OPEN' in var.get_browse_name().to_string():
                    # print(
                    #     'open' + values[var.get_browse_name().to_string()[2:]])
                    var.set_value(
                        0 if values[var.get_browse_name().to_string()[2:]] == 'True' or
                        values[var.get_browse_name().to_string()[2:]] == 'TRUE' else 1)
                    # print(
                    #     (1 if values[var.get_browse_name().to_string()[2:]] == 'True' or
                    #      values[var.get_browse_name().to_string()[2:]] == 'TRUE' else 0))

                elif 'STATUS_CLOSE' in var.get_browse_name().to_string():
                    # print(
                    #     'close' + values[var.get_browse_name().to_string()[2:]])
                    var.set_value(
                        0 if values[var.get_browse_name().to_string()[2:]] == 'True' or
                        values[var.get_browse_name().to_string()[2:]] == 'TRUE' else 1)
                    # print(
                    #     (1 if values[var.get_browse_name().to_string()[2:]] == 'True' or
                    #      values[var.get_browse_name().to_string()[2:]] == 'TRUE' else 0))
                elif 'STATUS' in var.get_browse_name().to_string() and \
                        'MODE_STATUS' not in var.get_browse_name().to_string():
                    print('status', values[var.get_browse_name().to_string()[2:]])
                    var.set_value(
                        values[var.get_browse_name().to_string()[2:]])
                    # print(values[var.get_browse_name().to_string()[2:]])

        except Exception as e:
            e
            print(str(e) + 'is an error')


def make_writable(node: object):
    '''
    Sets ALL variables of input node as writable

    @Param Node $node
    '''
    for var in node.get_variables():
        var.set_writable()


def create_timestamp(namespace: str, sector: object, bname: str, timestamp):
    '''
    Creates a switch object of the Node Class

    @Param string $namespace
    @Param Node $sector
    @Param string $bname
    @Param string $timestamp
    @return node switch
    '''

    try:
        ts = sector.add_object(namespace, bname)
        ts.add_variable(namespace, 'timestamp', timestamp)

        return ts
    except Exception as e:
        print(e)


def create_meter(namespace: str, sector: str, bname: str, deviceNo: str = None):
    '''
    Creates a Meter object of the Node Class of a given sector

    @Param str $namespace
    @Param str $sector
    @Param str $bname
    @Param str $deviceNo
    '''
    if sector.get_browse_name().to_string() == '2:MicroGrid':
        pass
    elif sector.get_browse_name().to_string() == '2:Generation':
        pass
    elif sector.get_browse_name().to_string() == '2:SmartHome':
        pass
    elif sector.get_browse_name().to_string() == '2:Transmission':
        pass
    else:
        raise Exception('Not a Valid Browse Name')

    try:
        meter = sector.add_object(namespace, bname)
        meter.add_variable(
            namespace, '{}.Measurement.Apparent'.format(bname), 0.0)
        meter.add_variable(
            namespace, '{}.Measurement.Frequency'.format(bname), 0.0)
        meter.add_variable(
            namespace, '{}.Measurement.L1_Current'.format(bname), 0.0)
        meter.add_variable(
            namespace, '{}.Measurement.L2_Current'.format(bname), 0.0)
        meter.add_variable(
            namespace, '{}.Measurement.L3_Current'.format(bname), 0.0)
        meter.add_variable(
            namespace, '{}.Measurement.Power_Factor'.format(bname), 0.0)
        meter.add_variable(
            namespace, '{}.Measurement.Reactive'.format(bname), 0.0)
        meter.add_variable(namespace, '{}.Measurement.Real'.format(bname), 0.0)
        meter.add_variable(namespace, '{}.Measurement.V1'.format(bname), 0.0)
        meter.add_variable(namespace, '{}.Measurement.V2'.format(bname), 0.0)
        meter.add_variable(namespace, '{}.Measurement.V3'.format(bname), 0.0)
        meter.add_variable(
            namespace, '{}.Measurement.VL1_L2'.format(bname), 0.0)
        meter.add_variable(
            namespace, '{}.Measurement.VL2_L3'.format(bname), 0.0)
        meter.add_variable(
            namespace, '{}.Measurement.VL3_VL1'.format(bname), 0.0)

        make_writable(meter)
        return meter
    except Exception as e:
        print(e)


def create_switch(namespace: str, sector: object, bname: str, STATUS: list, STATUS_OPEN: bool, STATUS_CLOSE: bool):
    '''
    Creates a switch object of the Node Class

    @Param string $namespace
    @Param Node $sector
    @Param string $bname
    @Param array $STATUS
    @Param bool $STATUS_OPEN
    @Param bool $STATUS_CLOSE
    @return node switch
    '''

    try:
        switch = sector.add_object(namespace, bname)
        switch.add_variable(namespace, '{}.STATUS'.format(
            bname), STATUS)  # [10] or [01]
        switch.add_variable(
            namespace, '{}.STATUS_CLOSE'.format(bname), STATUS_CLOSE)
        switch.add_variable(
            namespace, '{}.STATUS_OPEN'.format(bname), STATUS_OPEN)

        return switch
    except Exception as e:
        print(e)


def create_AMIMeter(namespace: str, sector: str, bname: str, deviceNo: str):
    '''
    Creates a AMI Meter object of the Node Class
    @Param string $namespace
    @Param string $sector
    @Param string $bname
    @Param string $deviceNo
    '''
    if sector.get_browse_name().to_string() == '2:MicroGrid':
        pass
    elif sector.get_browse_name().to_string() == '2:Generation':
        pass
    elif sector.get_browse_name().to_string() == '2:SmartHome':
        pass
    else:
        raise Exception('Not a valid browse name')

    try:
        AMIMeter = sector.add_object(namespace, bname)
        AMIMeter.add_variable(namespace, '{}.Voltage_L1'.format(bname), 0)
        AMIMeter.add_variable(namespace, '{}.Voltage_L2'.format(bname), 0)
        AMIMeter.add_variable(namespace, '{}.Voltage_L3'.format(bname), 0)
        AMIMeter.add_variable(namespace, '{}.Current_L1'.format(bname), 0)
        AMIMeter.add_variable(namespace, '{}.Current_L2'.format(bname), 0)
        AMIMeter.add_variable(namespace, '{}.Current_L3'.format(bname), 0)
        AMIMeter.add_variable(
            namespace, '{}.Active_Energy_KWh'.format(bname), 0)
        AMIMeter.add_variable(namespace, '{}.Power_Factor'.format(bname), 0)
        AMIMeter.add_variable(namespace, '{}.Power_Frequency'.format(bname), 0)

        make_writable(AMIMeter)
        return AMIMeter

    except Exception as e:
        print(e)
