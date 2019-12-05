import string

def intcode_program(intcodes):
    finished = False
    i = 0
    while not finished:
        padding = 0
        try:
            params_opcode = str(intcodes[i])
        except IndexError:
            break
        while len(params_opcode) < 5:
            params_opcode = '0' + params_opcode
            padding += 1
        param_modes = [int(params_opcode[2]), int(params_opcode[1]), int(params_opcode[0])]
        opcode = params_opcode[3:]
        if opcode[0] == '0':
            opcode = int(opcode[1])
        else:
            opcode = int(opcode)
        if opcode == 1:
            #print("add")
            if param_modes[0] == 0:
                param1 = intcodes[intcodes[i+1]]
            else:
                param1 = intcodes[i+1]
            if param_modes[1] == 0:
                param2 = intcodes[intcodes[i+2]]
            else:
                param2 = intcodes[i+2]
            param3 = int(intcodes[i+3])
            intcodes[param3] = param1 + param2
            i += 4
        elif opcode == 2:
            #print("multiply")
            if param_modes[0] == 0:
                param1 = intcodes[intcodes[i+1]]
            else:
                param1 = intcodes[i+1]
            if param_modes[1] == 0:
                param2 = intcodes[intcodes[i+2]]
            else:
                param2 = intcodes[i+2]
            param3 = intcodes[i+3]
            intcodes[param3] = param1 * param2
            i += 4
        elif opcode == 3:
            #print("input")
            param1 = int(intcodes[i+1])
            intcodes[param1] = int(input())
            i += 2
        elif opcode == 4:
            #print("output")
            param1 = int(intcodes[i+1])
            print(intcodes[param1])
            i += 2
        elif opcode == 5:
            # jump-if-true
            if param_modes[0] == 0:
                param1 = intcodes[intcodes[i+1]]
            else:
                param1 = intcodes[i+1]
            if param_modes[1] == 0:
                param2 = intcodes[intcodes[i+2]]
            else:
                param2 = intcodes[i+2]
            if param1 != 0:
                i = param2
            else:
                i += 3
        elif opcode == 6:
            # jump-if-false
            if param_modes[0] == 0:
                param1 = intcodes[intcodes[i+1]]
            else:
                param1 = intcodes[i+1]
            if param_modes[1] == 0:
                param2 = intcodes[intcodes[i+2]]
            else:
                param2 = intcodes[i+2]
            if param1 == 0:
                i = param2
            else:
                i += 3
        elif opcode == 7:
            # Less than
            if param_modes[0] == 0:
                param1 = intcodes[intcodes[i+1]]
            else:
                param1 = intcodes[i+1]
            if param_modes[1] == 0:
                param2 = intcodes[intcodes[i+2]]
            else:
                param2 = intcodes[i+2]
            param3 = intcodes[i+3]
            if param1 < param2:
                intcodes[param3] = 1
            else:
                intcodes[param3] = 0
            i += 4
        elif opcode == 8:
            # Greater than
            if param_modes[0] == 0:
                param1 = intcodes[intcodes[i+1]]
            else:
                param1 = intcodes[i+1]
            if param_modes[1] == 0:
                param2 = intcodes[intcodes[i+2]]
            else:
                param2 = intcodes[i+2]
            param3 = intcodes[i+3]
            if param1 == param2:
                intcodes[param3] = 1
            else:
                intcodes[param3] = 0
            i += 4
        elif opcode == 99:
            # halt
            break
    return intcodes


if __name__ == '__main__':
    intcodes_input = open('codes.txt', 'r').read()
    #intcodes_input = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
    intcodes = intcodes_input.split(',')
    intcodes = list(map(int, intcodes))
    intcodes = intcode_program(intcodes)  
    #print(intcodes)  
    
