import string
from math import inf

if __name__ == '__main__':
    wire_input = open('intersections.txt', 'r').read()
    wires = wire_input.split('\n')[:-1]
    closest_intersection_mhd = inf
    paths = []
    for wire in wires:
        min_steps = inf
        steps = 0
        path = {}
        moves = wire.split(',')
        pos_x = 0
        pos_y = 0
        pos = (pos_x,pos_y)
        for movement in moves:
            direction = movement[0]
            distance = int(movement[1:])
            if direction == 'R':
                #right
                for i in range(distance):
                    pos_x += 1
                    steps += 1
                    pos = (pos_x, pos_y)
                    for other_path in paths:
                        try:
                            intersect = other_path[pos]
                            sum_steps = steps + intersect[1]
                            manhattan_distance = abs(pos_x)+abs(pos_y)
                            if sum_steps < min_steps:
                                min_steps = sum_steps
                            if closest_intersection_mhd > manhattan_distance:
                                closest_intersection_mhd = manhattan_distance
                        except KeyError:
                            pass
                    try:
                        visited = path[pos]
                        pass
                    except KeyError:
                        path[pos] = [True, steps]
            elif direction == 'L':
                #left
                for i in range(distance):
                    pos_x -= 1
                    steps += 1
                    pos = (pos_x, pos_y)
                    for other_path in paths:
                        try:
                            intersect = other_path[pos]
                            sum_steps = steps + intersect[1]
                            manhattan_distance = abs(pos_x)+abs(pos_y)
                            if sum_steps < min_steps:
                                min_steps = sum_steps
                            if closest_intersection_mhd > manhattan_distance:
                                closest_intersection_mhd = manhattan_distance
                        except KeyError:
                            pass
                    try:
                        visited = path[pos]
                        pass
                    except KeyError:
                        path[pos] = [True, steps]
            elif direction == 'D':
                #down
                for i in range(distance):
                    pos_y -= 1
                    steps += 1
                    pos = (pos_x, pos_y)
                    for other_path in paths:
                        try:
                            intersect = other_path[pos]
                            sum_steps = steps + intersect[1]
                            manhattan_distance = abs(pos_x)+abs(pos_y)
                            if sum_steps < min_steps:
                                min_steps = sum_steps
                            if closest_intersection_mhd > manhattan_distance:
                                closest_intersection_mhd = manhattan_distance
                        except KeyError:
                            pass
                    try:
                        visited = path[pos]
                        pass
                    except KeyError:
                        path[pos] = [True, steps]
            elif direction == 'U':
                #up
                for i in range(distance):
                    pos_y += 1
                    steps += 1
                    pos = (pos_x, pos_y)
                    for other_path in paths:
                        try:
                            intersect = other_path[pos]
                            sum_steps = steps + intersect[1]
                            manhattan_distance = abs(pos_x)+abs(pos_y)
                            if sum_steps < min_steps:
                                min_steps = sum_steps
                            if closest_intersection_mhd > manhattan_distance:
                                closest_intersection_mhd = manhattan_distance
                        except KeyError:
                            pass
                    try:
                        visited = path[pos]
                        pass
                    except KeyError:
                        path[pos] = [True, steps]
        paths.append(path)
    print(closest_intersection_mhd)
    print(min_steps)


    

    
    
    
