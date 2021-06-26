import sys
import opcua
from random import randint
import constant


def setting_values(node: object, values: dict,):
    '''
    Set values for each individual variable of input Node.
    '''
    # Set Values for IED Meters.
    if 'IED' in node.get_browse_name().to_string():
        try:
            for var in node.get_variables():
                is_correct_value = False

                for val in constant.IED_VALUES:
                    if val in var.get_browse_name().to_string():
                        is_correct_value = True

                if is_correct_value:
                    var.set_value(
                        float(values[var.get_browse_name().to_string()[2:]]))

        except Exception as e:
            print(str(e) + ' is an error')

    # Set Values for AMI Meters. Don need to care.
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
    # Set Values for Switches.
    else:
        try:
            for var in node.get_variables():
                is_correct_value = False

                for val in constant.SWITCH_VALUES:
                    if val in var.get_browse_name().to_string():
                        is_correct_value = True

                print(var.get_browse_name().to_string())
                if is_correct_value:
                    if 'OPEN' in var.get_browse_name().to_string() or 'CLOSE' in var.get_browse_name().to_string():
                        var.set_value(
                            0 if values[var.get_browse_name().to_string()[2:]] == 'True' or
                            values[var.get_browse_name().to_string()[2:]] == 'TRUE' else 1)
                    else:
                        var.set_value(
                            values[var.get_browse_name().to_string()[2:]])

        except Exception as e:
            print(str(e) + 'is an error')


def create_timestamp(namespace: str, sector: object, bname: str, timestamp):
    '''
    Creates a Timestamp object of the Node Class of a given sector.
    '''
    try:
        ts = sector.add_object(namespace, bname)
        ts.add_variable(namespace, 'timestamp', timestamp)

        return ts
    except Exception as e:
        print(e)


def create_meter(namespace: str, sector: str, bname: str):
    '''
    Creates a Meter object of the Node Class of a given sector.
    '''
    try:
        meter = sector.add_object(namespace, bname)
        for val in constant.IED_VALUES:
            meter.add_variable(
                namespace, '{}.{}'.format(bname, val), 0.0)
        make_writable(meter)
        return meter
    except Exception as e:
        print(e)


def create_switch(namespace: str, sector: object, bname: str):
    '''
    Creates a switch object of the Node Class.
    '''
    try:
        switch = sector.add_object(namespace, bname)
        for val in constant.SWITCH_VALUES:
            switch.add_variable(
                namespace, '{}.{}'.format(bname, val), 0.0)
        return switch
    except Exception as e:
        print(e)


# Don care.
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


def make_writable(node: object):
    '''
    Sets ALL variables of input node as writable.
    '''
    for var in node.get_variables():
        var.set_writable()
