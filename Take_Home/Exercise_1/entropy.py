# this is just a simple program to calculate entropy

from math import log

def entropy(param_list):
    total = sum(param_list)
    print('sum:', total)
    
    params_log = [-((param/total)*(log((param/total),2))) for param in param_list]
    print('logs results:', params_log)

    entropy = sum(params_log)
    print('entropy:', entropy)


if __name__ == '__main__':
    while True:
        inputs_number = int(input('Inputs number: '))
        inputs = [int(input('Enter number: ')) for i in range(inputs_number)]
        entropy(inputs)
