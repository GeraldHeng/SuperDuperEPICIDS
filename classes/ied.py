from colorama import init, Fore, Back, Style
import helpers.client_helper_funcs as helper
import numpy as np
from helpers.constant import *


class Ied:
    def __init__(self, name=None, current=None, voltage=None, power_apparent=None, power_reactive=None,
                 power_real=None, origin=None, platform='real_epic'):
        '''
        @Params
        String name - name of the ied.
        List current - current values.
        List voltage - voltage values.
        List power_apparent - power_apparent values.
        List power_reactive - power_reactive values.
        List power_real - power_real values.
        '''
        self.name = name
        self.type = 'ied'
        self.current = current
        self.voltage = voltage
        self.power_apparent = power_apparent
        self.power_reactive = power_reactive
        self.power_real = power_real
        self.origin = origin
        self.consistent_status = True
        self.consistency_message = 'Consistent'
        self.platform = platform

    def introduce(self):
        '''
        Introduce ied by printing values.
        '''
        print(self.name
              + ' - current: ' + str(self.current) +
              ' voltage: ' + str(self.voltage) +
                ' power_apparent: ' + str(self.power_apparent) +
                ' power_reactive: ' + str(self.power_reactive) +
                ' power_real: ' + str(self.power_real))

    def check_off_consistency(self):
        '''
        Using corresponding switch of IED, if switch is OFF(OPEN) then
        current, voltage and power should be less than or equal to delta.
        '''
        # print(self.name)
        is_consistent = True

        # Current
        if np.less(self.current, CURRENT_MARGIN).all():
            # print(Fore.GREEN + 'current is consistent')
            v = 0
        else:
            print(Fore.RED + 'current is NOT consistent')
            is_consistent = False

        # Voltage
        # if np.less(self.voltage, VOLTAGE_MARGIN).all():
        #     # print(Fore.GREEN + 'voltage is consistent')
        #     v = 0
        # else:
        #     print(Fore.RED + 'voltage is NOT consistent')
        #     is_consistent = False
        # print('current voltage:', abs(self.voltage))
        # print('margin voltage:', VOLTAGE_MARGIN)
        # print()

        # Power Apparent
        if np.less(self.power_apparent, POWER_MARGIN).all():
            # print(Fore.GREEN + 'power apparent is consistent')
            v = 0
        else:
            print(Fore.RED + 'power apparent is NOT consistent')
            is_consistent = False

        # Power Reactive
        if np.less(self.power_reactive, POWER_MARGIN).all():
            # print(Fore.GREEN + 'power reactive is consistent')
            v = 0
        else:
            print(Fore.RED + 'power reactive is NOT consistent')
            is_consistent = False

        # Power Real
        if np.less(self.power_real, POWER_MARGIN).all():
            # print(Fore.GREEN + 'power real is consistent')
            v = 0
        else:
            print(Fore.RED + 'power real is NOT consistent')
            is_consistent = False

        if is_consistent:
            # print()
            self.consistent_status = True
            self.consistency_message = 'Consistent'
            return True
        else:
            self.consistency_message = 'IED Status is not consistent, should be 0'
            self.consistent_status = False
            print(Fore.RED + 'The current values are: ')
            self.introduce()
            print()

    @staticmethod
    def define_ied(node_name, node_dict, var_name, var_dict, server, origin):
        '''
        Define ied with values.
        @Param 
        String node_name - eg. Generation.GIED1.Measurement.
        Dict node_dict - where the node is stored.
        String var_name - variable name to define for var_dict.
        Dict var_dict - store switch/ied object.
        Client server - a client to server.
        '''
        # Define I (current) - i + var_name
        # Define V (voltage) - v + var_name
        # Define P (power) - p + var_name
        # TODO:Find a way to make this modular, don need the name for voltage, current and power.
        # I (current)
        current = np.array(
            [helper.get_node_value(node_name + '.Measurement.L1_Current', server, node_dict),
             helper.get_node_value(
                 node_name + '.Measurement.L2_Current', server, node_dict),
             helper.get_node_value(node_name + '.Measurement.L3_Current', server, node_dict)])

        # V (voltage)
        voltage = np.array(
            [helper.get_node_value(node_name + '.Measurement.V1', server, node_dict),
             helper.get_node_value(
                 node_name + '.Measurement.V2', server, node_dict),
             helper.get_node_value(
                 node_name + '.Measurement.V3', server, node_dict),
             helper.get_node_value(
                 node_name + '.Measurement.VL1_L2', server, node_dict),
             helper.get_node_value(
                 node_name + '.Measurement.VL2_L3', server, node_dict),
             helper.get_node_value(node_name + '.Measurement.VL3_VL1', server, node_dict)])

        # P (power)
        # Apparent
        power_apparent = np.array(
            [helper.get_node_value(node_name + '.Measurement.Apparent', server, node_dict)])

        # Reactive
        power_reactive = np.array(
            [helper.get_node_value(node_name + '.Measurement.Reactive', server, node_dict)])

        # Real
        power_real = np.array(
            [helper.get_node_value(node_name + '.Measurement.Real', server, node_dict)])

        var_dict[var_name] = Ied(var_name, current, voltage,
                                 power_apparent, power_reactive,
                                 power_real, origin)

    @staticmethod
    def define_ied_dt(var_name, values, var_dict):
        '''
        Define ied with values.
        @Param 
        Dict values - where is values of ied is temp store at.
        String var_name - variable name to define for var_dict.
        Dict var_dict - store switch/ied object.
        '''
        print(var_name)
        # I (current)
        current = np.array(
            [values['Ia'], values['Ib'], values['Ic']])

        # V (voltage)
        voltage = np.array(
            [values['Vca'], values['Vbc'], values['Vab']])

        var_dict[var_name] = Ied(
            name=var_name, current=current, voltage=voltage, platform='dt')
