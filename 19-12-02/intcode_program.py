import string

def intcode_program(intcodes):
    for i in range(0,len(intcodes),4):
        if intcodes[i] == 1:
            intcodes[intcodes[i+3]] = intcodes[intcodes[i+1]] + intcodes[intcodes[i+2]]
        elif intcodes[i] == 2:
            intcodes[intcodes[i+3]] = intcodes[intcodes[i+1]] * intcodes[intcodes[i+2]]
        elif intcodes[i] == 99:
            break
    return intcodes


if __name__ == '__main__':
    intcodes_input = open('intcodes.txt', 'r').read()
    intcodes = intcodes_input.split(',')
    for noun in range(0,99):
        for verb in range(0,99):
            _intcodes = list(map(int, intcodes))
            _intcodes[1] = noun
            _intcodes[2] = verb
            _intcodes = intcode_program(_intcodes)
            if _intcodes[0] == 19690720:
                print('noun: %s'%noun)
                print('verb: %s'%verb)
                print(100*noun+verb)
                exit()
    
    
