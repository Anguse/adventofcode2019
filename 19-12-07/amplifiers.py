from string import split
from copy import deepcopy
from threading import Thread, Lock
from itertools import permutations

amp1_buffer = []
amp2_buffer = []
amp3_buffer = []
amp4_buffer = []
amp5_buffer = []

mutex = Lock()

thrust = 0

def set_output(amplifier, value):

    global amp1_buffer, amp2_buffer, amp3_buffer, amp4_buffer, amp5_buffer, mutex
    mutex.acquire()
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
    mutex.release()

def get_input(amplifier, arg_ptr):

    global amp1_buffer, amp2_buffer, amp3_buffer, amp4_buffer, amp5_buffer, mutex
    done = False
    while not done:
        mutex.acquire()
        try:
            if amplifier == 'a':
                value = amp1_buffer[arg_ptr]
            elif amplifier == 'b':
                value = amp2_buffer[arg_ptr]
            elif amplifier == 'c':
                value = amp3_buffer[arg_ptr]
            elif amplifier == 'd':
                value = amp4_buffer[arg_ptr]
            elif amplifier == 'e':
                value = amp5_buffer[arg_ptr]
            mutex.release()
            return value
        except IndexError:
            # wait for other amplifiers
            mutex.release()
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

    global thrust, mutex
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
            thrust = output
            finished = True
            break
    return

def run_amplifier_setup(intcodes, phase_settings):

    global amp1_buffer, amp2_buffer, amp3_buffer, amp4_buffer, amp5_buffer, mutex
    amps = ['a', 'b', 'c', 'd', 'e']
    mutex.acquire()
    amp1_buffer = [0]
    amp2_buffer = []
    amp3_buffer = []
    amp4_buffer = []
    amp5_buffer = []
    mutex.release()

    for i,amp in enumerate(amps):
        t = Thread(target=intcode_program, args=(deepcopy(intcodes), amp, phase_settings[i]))
        t.start()
        amp_threads.append(t)
    for t in amp_threads:
        t.join()
    return
    
if __name__ == '__main__':

    intcodes_input = open('input.txt', 'r').read()
    intcodes = intcodes_input.split(',')
    intcodes = list(map(int, intcodes))
    
    sequences = permutations([5,6,7,8,9])
    amp_threads = []
    max_thrust = 0

    for phase_settings in list(sequences):
        run_amplifier_setup(intcodes, phase_settings)
        if thrust > max_thrust:
            max_thrust = thrust
    print(max_thrust)