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
    intersections_input = open('intersections.txt', 'r').read()
    intersections = intersections_input.split('\n')
    map = []
    for i in range(100000):
        part_map = []
        for j in range(100000):
            part_map.append(0)
        map.append(part_map)
    #_intcodes = list(map(int, crossings))
    map[0][0] = -1
    closest_intersection_mhd = 50000
    for wire in intersections:
        crossings = wire.split(',')
        pos_x = 50000
        pos_y = 50000
        print(closest_intersection_mhd)
        for movement in crossings:
            #print(pos_x)
            #print(pos_y)
            direction = movement[0]
            distance = int(movement[1:])
            if direction == 'R':
                #right
                print('right')
                print(distance)
                for i in range(distance):
                    pos_x += 1
                    if map[pos_x][pos_y] == 1:
                        # intersection
                        map[pos_x][pos_y] = 2
                        manhattan_distance = abs(pos_x-50000)+abs(pos_y-50000)
                        if closest_intersection_mhd > manhattan_distance:
                            closest_intersection_mhd = manhattan_distance
                    elif map[pos_x][pos_y] == 0:
                        map[pos_x][pos_y] = 1
            elif direction == 'L':
                #left
                for i in range(distance):
                    pos_x -= 1
                    if map[pos_x][pos_y] == 1:
                        # intersection
                        map[pos_x][pos_y] = 2
                        manhattan_distance = abs(pos_x-50000)+abs(pos_y-50000)
                        if closest_intersection_mhd > manhattan_distance:
                            closest_intersection_mhd = manhattan_distance
                    elif map[pos_x][pos_y] == 0:
                        map[pos_x][pos_y] = 1
            elif direction == 'D':
                # down
                for i in range(distance):
                    pos_y -= 1
                    if map[pos_x][pos_y] == 1:
                        # intersection
                        map[pos_x][pos_y] = 2
                        manhattan_distance = abs(pos_x-50000)+abs(pos_y-50000)
                        if closest_intersection_mhd > manhattan_distance:
                            closest_intersection_mhd = manhattan_distance
                    elif map[pos_x][pos_y] == 0:
                        map[pos_x][pos_y] = 1
            elif direction == 'U':
                # up
                for i in range(distance):
                    pos_y += 1
                    if map[pos_x][pos_y] == 1:
                        # intersection
                        map[pos_x][pos_y] = 2
                        manhattan_distance = abs(pos_x-50000)+abs(pos_y-50000)
                        if closest_intersection_mhd > manhattan_distance:
                            closest_intersection_mhd = manhattan_distance
                    elif map[pos_x][pos_y] == 0:
                        map[pos_x][pos_y] = 1
        print(closest_intersection_mhd)


    

    
    
    
