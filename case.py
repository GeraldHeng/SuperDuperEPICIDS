import numpy as np
import constant
from colorama import init, Fore, Back, Style

# Generate different kind of case, summation case...
# TODO: NEED TO WORK ON GENERATING MODULAR CASES.


class Case:
    def __init__(self, name, definition, c_type, items):
        '''
        @Params
        '''
        self.name = name
        self.c_type = c_type
        # current, power, voltage
        self.definition = definition
        self.items = items

    def get_result(self):
        '''
        Find the result using values and c_type by what definition it is.
        '''
        if self.c_type == 'summation_equal':
            summations = []
            for values in self.items:
                # print([item.current for item in values])
                if self.definition == 'current':
                    summations.append(sum([item.current for item in values]))

            is_success = True
            for summation in summations:
                for summation2 in summations:
                    if np.less(abs(summation - summation2),
                               constant.CURRENT_MARGIN).all():
                        is_success
                    else:
                        is_success = False

            if is_success:
                return True
            else:
                print(Fore.RED + 'Case ' + self.name + ' is NOT consistent')
                for i in range(0, len(summations)):
                    print('summation', i+1, 'values:', summations[i])
                print('abs', abs(summations[0] - summations[1]))
                print()
                return False
