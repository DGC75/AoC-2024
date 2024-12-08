from collections import ChainMap
from itertools import combinations

filename = 'input'


def is_in_boundaries(t, x,y):
    if (t[0] >= 0 and t[0] < x) and (t[1] >= 0 and t[1] < y):
        return True
    return False

def get_antinodes(l, x, y):
    retval = []

    #select two distinct points
    distinct_couple_points = [list(subset) for subset in combinations(l, 2)]
    #print(distinct_couple_points)
    

    for couple in distinct_couple_points:
        dx = couple[0][0] - couple[1][0]
        dy = couple[0][1] - couple[1][1]
        #print(dx, dy)
        candidate_antinode_1 = (couple[0][0] + dx, couple[0][1] + dy)
        candidate_antinode_2 = (couple[1][0] - dx, couple[1][1] - dy)


        #print(candidate_antinode_1, candidate_antinode_2)
        if is_in_boundaries(candidate_antinode_1, x,y):
            retval.append(candidate_antinode_1)
        if is_in_boundaries(candidate_antinode_2, x,y):
            retval.append(candidate_antinode_2)

    return retval

if __name__ == '__main__':
    #parse input

    input = []
    with open(filename) as file:
        for row, line in enumerate(file):
            line = line.split()
            input.append([])
            for char in line[0]:
                input[row].append(char)

    for line in input:
        print(line)

    #process input

    antennas = dict()

    for x, line in enumerate(input):
        for y, char in enumerate(line):
            if not(char == '.'):
                l = antennas.get(char)
                
                if(l):
                    l.append((x,y))
                    antennas.update({char: l})
                else:
                    antennas.update({char: [(x,y)]})



    keys = list(antennas.keys())
    print(keys)
    antinodes = []
    for key in keys:
        antinodes.append(get_antinodes(antennas[key], len(input[0]), len(input)))
        antinodes[0].sort()
        print(antinodes)
    antinodes = [x for xs in antinodes for x in xs]
    antinodes = list(dict.fromkeys(antinodes))

    new_input = input.copy()
    for antinode in antinodes:
        new_input[antinode[0]][antinode[1]] = '#'

    for line in new_input:
        print(line)

    print(len(antinodes))
    retval = 0
