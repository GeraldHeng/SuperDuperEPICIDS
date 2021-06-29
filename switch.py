from colorama import init, Fore, Back, Style
import helpers.client_helper_funcs as helper


class Switch:
    def __init__(self, name, is_close, is_open, status, connected_to, origin):
        '''
        @Params
        String name - name of the switch.
        int is_close - 0 or 1.
        int is_open - 0 or 1.
        String status (UI) - [01] or [10].
        '''
        self.name = name
        self.type = 'switch'
        self.is_close = is_close
        self.is_open = is_open
        self.status = status
        self.connected_to = connected_to
        self.origin = origin
        self.consistent_status = True
        self.consistency_message = 'Consistent'

    def introduce(self):
        '''
        Introduce switch by printing values.
        '''
        print(self.name
              + ' - is_close: ' + str(self.is_close) +
              ' is_open: ' + str(self.is_open) +
              ' status: ' + str(self.status))

    def check_consistency(self):
        '''
        Check value of is_close, is_open and status align with each other.
        2 case.
        is_close is 1 and is_open is 0 then status is [10]
        is_close is 0 and is_open is 1 then status is [01]
        '''
        if \
            (self.is_close == 1 and self.is_open == 0 and
             self.status == '[10]') or \
            (self.is_close == 0 and self.is_open == 1 and
             self.status == '[01]'):
            self.consistent_status = True
            self.consistency_message = 'Consistent'
            return True
        else:
            print(Fore.RED + self.name + ' switch status is NOT consistent')
            print(Fore.RED + 'The current values are: ')
            self.introduce()
            print()
            self.consistent_status = False
            self.consistency_message = 'Switch Status is not consistent'
            return False

    def is_switch_close(self):
        '''
        Check is switch is close(ON) or open(OFF).
        '''
        return self.is_close == 0 and self.is_open == 1 and self.status == '[01]'

    @ staticmethod
    def define_switch(node_name, node_dict, var_name, var_dict, server, connected_to, origin):
        '''
        Define switch with values.
        String node_name - eg. Generation.Q1.
        Dict node_dict - where the node is stored.
        String var_name - variable name to define for var_dict.
        Dict var_dict - store switch/ied object.
        Client server - a client to server.
        '''
        # Why do we need _ and _ui.
        is_close = 1 if helper.get_node_value(
            node_name + '.STATUS_CLOSE', server, node_dict) else 0

        is_open = 1 if helper.get_node_value(
            node_name + '.STATUS_OPEN', server, node_dict) else 0

        status = helper.get_node_value(
            node_name + '.STATUS', server, node_dict)

        var_dict[var_name] = Switch(
            var_name, is_close, is_open, status, connected_to, origin)
