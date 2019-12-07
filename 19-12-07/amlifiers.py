import string
import threading
import time
from itertools import permutations

amp1_buffer = []
amp2_buffer = []
amp3_buffer = []
amp4_buffer = []
amp5_buffer = []
thrusts = []

def set_output(amplifier, value):
    print("amp %s outputs %d"%(amplifier, value))
    if amplifier == 'a':
        amp2_buffer.append(value)
    elif amplifier == 'b':
        amp3_buffer.append(value)
    elif amplifier == 'c':
        amp4_buffer.append(value)
    elif amplifier == 'd':
        amp5_buffer.append(value)
    elif amplifier == 'e':
        amp1_buffer.append(value)

def get_input(amplifier, arg_ptr):
    done = False
    count = 0
    while not done:
        # To avoid program getting stuck
        if count > 10:
            exit()
        try:
            if amplifier == 'a':
                return amp1_buffer[arg_ptr]
            elif amplifier == 'b':
                return amp2_buffer[arg_ptr]
            elif amplifier == 'c':
                return amp3_buffer[arg_ptr]
            elif amplifier == 'd':
                return amp4_buffer[arg_ptr]
            elif amplifier == 'e':
                return amp5_buffer[arg_ptr]
        except IndexError:
            # wait for other amplifiers
            time.sleep(.001)
            count += 1
            continue
        break

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

def intcode_program(intcodes, amplifier, phase_setting):
    finished = False
    arg_ptr = -1
    i_ptr = 0
    output = 0
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
            if arg_ptr == -1:
                intcodes[params] = phase_setting
            else:
                intcodes[params] = get_input(amplifier, arg_ptr)
            arg_ptr += 1
            i_ptr += 2
        elif opcode == 4:
            # output
            params = intcodes[i_ptr+1]
            set_output(amplifier, intcodes[params])
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
            thrusts.append(output)
            finished = True
            break
    return


if __name__ == '__main__':
    intcodes_input = open('input.txt', 'r').read()
    intcodes = intcodes_input.split(',')
    intcodes = list(map(int, intcodes))
    
    sequences = permutations([5,6,7,8,9])
    amps = ['a', 'b', 'c', 'd', 'e']
    threads = []
    for seq in list(sequences):
        amp1_buffer = [0]
        amp2_buffer = []
        amp3_buffer = []
        amp4_buffer = []
        amp5_buffer = []
        for i,amp in enumerate(amps):
            t = threading.Thread(target=intcode_program, args=(intcodes, amp, seq[i]))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
    print("max thrust %d"%max(thrusts))
    