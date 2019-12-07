import string
from itertools import permutations

def get_params(param_modes, intcodes, i_ptr):
    if param_modes[0] == 0:
        param1 = intcodes[intcodes[i_ptr+1]]
    else:
        param1 = intcodes[i_ptr+1]
    if param_modes[1] == 0:
        param2 = intcodes[intcodes[i_ptr+2]]
    else:
        param2 = intcodes[i_ptr+2]
    param3 = intcodes[i_ptr+3]
    return [param1, param2, param3]

def intcode_program(intcodes, args):
    finished = False
    arg_ptr = 0
    i_ptr = 0
    while not finished:
        params_opcode = str(intcodes[i_ptr])
        while len(params_opcode) < 5:
            params_opcode = '0' + params_opcode
        param_modes = [int(params_opcode[2]), int(params_opcode[1]), int(params_opcode[0])]
        opcode = params_opcode[3:]
        if opcode[0] == '0':
            opcode = int(opcode[1])
        else:
            opcode = int(opcode)
        if opcode == 1:
            # add
            params = get_params(param_modes, intcodes, i_ptr)
            intcodes[params[2]] = params[0] + params[1]
            i_ptr += 4
        elif opcode == 2:
            # multiply
            params = get_params(param_modes, intcodes, i_ptr)
            intcodes[params[2]] = params[0] * params[1]
            i_ptr += 4
        elif opcode == 3:
            # input
            params = intcodes[i_ptr+1]
            intcodes[params] = args[arg_ptr]
            arg_ptr += 1
            i_ptr += 2
        elif opcode == 4:
            # output
            params = intcodes[i_ptr+1]
            #print(intcodes[params])
            output = intcodes[params]
            i_ptr += 2
        elif opcode == 5:
            # jump-if-true
            params = get_params(param_modes, intcodes, i_ptr)
            if params[0] != 0:
                i_ptr = params[1]
            else:
                i_ptr += 3
        elif opcode == 6:
            # jump-if-false
            params = get_params(param_modes, intcodes, i_ptr)
            if params[0] == 0:
                i_ptr = params[1]
            else:
                i_ptr += 3
        elif opcode == 7:
            # less than
            params = get_params(param_modes, intcodes, i_ptr)
            if params[0] < params[1]:
                intcodes[params[2]] = 1
            else:
                intcodes[params[2]] = 0
            i_ptr += 4
        elif opcode == 8:
            # greater than
            params = get_params(param_modes, intcodes, i_ptr)
            if params[0] == params[1]:
                intcodes[params[2]] = 1
            else:
                intcodes[params[2]] = 0
            i_ptr += 4
        elif opcode == 99:
            # halt
            finished = True
            break
    return output

if __name__ == '__main__':
    intcodes_input = open('input.txt', 'r').read()
    intcodes = intcodes_input.split(',')
    intcodes = list(map(int, intcodes))
    max_current = 0

    sequences = permutations([0,1,2,3,4])
    for seq in list(sequences):
            amp1 = intcode_program(intcodes, [seq[0],0])
            amp2 = intcode_program(intcodes, [seq[1],amp1])
            amp3 = intcode_program(intcodes, [seq[2],amp2])
            amp4 = intcode_program(intcodes, [seq[3],amp3])
            amp5 = intcode_program(intcodes, [seq[4],amp4])
            if amp5 > max_current:
                max_current = amp5
    print(max_current)
    '''
    for i in range(4):
        for ii in range(4):
            for iii in range(4):
                for iiii in range(4):
                    for iiiii in range(4):
                        
    print(max_current)
    '''