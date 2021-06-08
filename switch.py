from colorama import init, Fore, Back, Style
import helpers.client_helper_funcs as helper

class Switch:
    def __init__(self, name, is_close, is_open, status):
        '''
        @Params
        String name - name of the switch.
        int is_close - 0 or 1.
        int is_open - 0 or 1.
        String status (UI) - [01] or [10].
        '''
        self.name = name
        self.is_close = is_close
        self.is_open = is_open
        self.status = status

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
        is_cose is 1 and is_open is 0 then status is [10]
        is_cose is 0 and is_open is 1 then status is [01]
        '''
        if \
            (self.is_close == 1 and self.is_open == 0 and
             self.status == '[10]') or \
            (self.is_close == 0 and self.is_open == 1 and
             self.status == '[01]'):
            print(Fore.GREEN + self.name + ' switch status is consistent')
            print()
            return True
        else:
            print(Fore.RED + self.name + ' switch status is NOT consistent')
            print(Fore.RED + 'The current values are: ')
            self.introduce()
            print()
            return False

    @ staticmethod
    def define_switch(node_name, node_dict, var_name, var_dict, server):
        '''
        Define switch with values.
        @Param
        String node_name - eg. Generation.Q1.
        Dict node_dict - where the node is stored.
        String var_name - variable name to define for var_dict.
        Dict var_dict - store switch/ied object.
        Client server - a client to server.
        '''
        # Why do we need _ and _ui.
        is_close = 0 if helper.get_node_value(
            node_name + '.STATUS_CLOSE', server, node_dict) else 1

        is_open = 0 if helper.get_node_value(
            node_name + '.STATUS_OPEN', server, node_dict) else 1

        status = helper.get_node_value(
            node_name + '.STATUS', server, node_dict)

     
        var_dict[var_name] = Switch(var_name, is_close, is_open, status)
