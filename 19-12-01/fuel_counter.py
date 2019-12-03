
import string
from math import floor

def fuel_estimator(mass):
    part_fuel = floor(int(mass)/3)-2
    if part_fuel > 6:
        part_fuel += fuel_estimator(part_fuel)
    return part_fuel


if __name__ == '__main__':
    modules_input = open('modules.txt', 'r').read()
    module_masses = modules_input.split('\n')
    module_masses = module_masses[:-1]
    req_fuel = 0
    for mass in module_masses:
        req_fuel += fuel_estimator(mass)
    print(req_fuel)
