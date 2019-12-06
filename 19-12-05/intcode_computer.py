import string

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

def intcode_program(intcodes):
    finished = False
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
            intcodes[params] = int(input())
            i_ptr += 2
        elif opcode == 4:
            # output
            params = intcodes[i_ptr+1]
            print(intcodes[params])
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
    return intcodes

if __name__ == '__main__':
    intcodes_input = open('codes.txt', 'r').read()
    intcodes = intcodes_input.split(',')
    intcodes = list(map(int, intcodes))
    intcodes = intcode_program(intcodes)  
    
