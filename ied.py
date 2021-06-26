from colorama import init, Fore, Back, Style
import helpers.client_helper_funcs as helper
import numpy as np
import constant


class IED:
    def __init__(self, name, current, voltage, power_apparent, power_reactive,
                 power_real):
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
        self.current = current
        self.voltage = voltage
        self.power_apparent = power_apparent
        self.power_reactive = power_reactive
        self.power_real = power_real

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
        # print(Fore.GREEN + self.name + ' corresponding switch is OFF')

        # Current
        if np.less(self.current, constant.CURRENT_MARGIN).all():
            # print(Fore.GREEN + 'current is consistent')
            v = 0
        else:
            print(Fore.RED + 'current is NOT consistent')
            is_consistent = False
        # print('current current:', abs(self.current))
        # print('margin current:', constant.CURRENT_MARGIN)
        # print()

        # Voltage
        # if np.less(self.voltage, constant.VOLTAGE_MARGIN).all():
        #     # print(Fore.GREEN + 'voltage is consistent')
        #     v = 0
        # else:
        #     print(Fore.RED + 'voltage is NOT consistent')
        #     is_consistent = False
        # print('current voltage:', abs(self.voltage))
        # print('margin voltage:', constant.VOLTAGE_MARGIN)
        # print()

        # Power Apparent
        if np.less(self.power_apparent, constant.POWER_MARGIN).all():
            # print(Fore.GREEN + 'power apparent is consistent')
            v = 0
        else:
            print(Fore.RED + 'power apparent is NOT consistent')
            is_consistent = False
        # print('current power apparent:', abs(self.power_apparent))
        # print('margin power:', constant.POWER_MARGIN)
        # print()

        # Power Reactive
        if np.less(self.power_reactive, constant.POWER_MARGIN).all():
            # print(Fore.GREEN + 'power reactive is consistent')
            v = 0
        else:
            print(Fore.RED + 'power reactive is NOT consistent')
            is_consistent = False
        # print('current power reactive:', abs(self.power_reactive))
        # print('margin power reactive:', constant.POWER_MARGIN)
        # print()

        # Power Real
        if np.less(self.power_real, constant.POWER_MARGIN).all():
            # print(Fore.GREEN + 'power real is consistent')
            v = 0
        else:
            print(Fore.RED + 'power real is NOT consistent')
            is_consistent = False
        # print('current power real:', abs(self.power_real))
        # print('margin power real:', constant.POWER_MARGIN)
        # print()

        if is_consistent:
            # print()
            return True
        else:
            print(Fore.RED + 'The current values are: ')
            self.introduce()
            print()

    @staticmethod
    def define_ied(node_name, node_dict, var_name, var_dict, server):
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

        # I (current)
        current = np.array(
            [helper.get_node_value(node_name + '.L1_Current', server, node_dict),
             helper.get_node_value(
                 node_name + '.L2_Current', server, node_dict),
             helper.get_node_value(
                 node_name + '.L2_Current', server, node_dict),
             helper.get_node_value(node_name + '.L3_Current', server, node_dict)])

        # V (voltage)
        voltage = np.array(
            [helper.get_node_value(node_name + '.V1', server, node_dict),
             helper.get_node_value(node_name + '.V2', server, node_dict),
             helper.get_node_value(node_name + '.V3', server, node_dict),
             helper.get_node_value(node_name + '.VL1_L2', server, node_dict),
             helper.get_node_value(node_name + '.VL2_L3', server, node_dict),
             helper.get_node_value(node_name + '.VL3_VL1', server, node_dict)])

        # P (power)
        # Apparent
        power_apparent = np.array(
            [helper.get_node_value(node_name + '.Apparent', server, node_dict)])

        # Reactive
        power_reactive = np.array(
            [helper.get_node_value(node_name + '.Reactive', server, node_dict)])

        # Real
        power_real = np.array(
            [helper.get_node_value(node_name + '.Real', server, node_dict)])

        var_dict[var_name] = IED(var_name, current, voltage,
                                 power_apparent, power_reactive,
                                 power_real)
