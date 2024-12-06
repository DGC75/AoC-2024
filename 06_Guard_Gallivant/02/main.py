
from copy import deepcopy

filename = 'input'

def find_guard_coord(char, matrix2d):
    for y, row in enumerate(matrix2d):
        for x, col in enumerate(matrix2d[0]):
            if matrix2d[x][y] == char:
                return [str(x),str(y)]


def in_boundaries(guard_coord, matrix2d):
    y_bound = len(matrix2d)
    x_bound = len(matrix2d[0])
    x = int(guard_coord[0])
    y = int(guard_coord[1])

    if((x >= 0 and x < x_bound) and (y >= 0 and y < y_bound)):
        return True
    
    return False

def calculate_next_pos(orientation, matrix2d, x,y):
    
    if orientation == '^':
        candidate_next_pos = [x-1, y]
    elif orientation == '>':
        candidate_next_pos = [x, y+1]
    elif orientation == '<':
        candidate_next_pos = [x, y-1]
    elif orientation == 'v':
        candidate_next_pos = [x+1, y]
    if(in_boundaries(candidate_next_pos, matrix2d) and matrix2d[candidate_next_pos[0]][candidate_next_pos[1]] == '#'):
        if orientation == '^':
            orientation = '>'
            candidate_next_pos = [x,y]
        elif orientation == '>':
            orientation = 'v'
            candidate_next_pos = [x,y]
        elif orientation == '<':
            orientation = '^'
            candidate_next_pos = [x,y]
        elif orientation == 'v':
            orientation = '<'
            candidate_next_pos = [x,y]
    

    candidate_next_pos.append(orientation)
    return candidate_next_pos

def move(guard_coord,matrix2d):
 

    x = int(guard_coord[0])
    y = int(guard_coord[1])
    orientation = guard_coord[2]
 
    next_pos = calculate_next_pos(orientation, matrix2d, x,y)

    return next_pos

def place_obstacle(matr, position):
    new = deepcopy(matr)
    new[position[0]][position[1]] = '#'

    return new



def loop_detected(matrix2d, position, start_pos):
    stack = [start_pos, position]
    while(in_boundaries(start_pos, matrix2d)):

        start_pos = move(start_pos, matrix2d)
        
        if((start_pos in stack)):
            #for pos in stack:
            #    print(pos)
            #print()
            return True
        else:
            stack.append(start_pos)
            
    return False

if __name__ == "__main__":
    matrix2d = []

    count_path = 0

    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
        i = 0
        for line in lines:
            matrix2d.append([])
            arr = matrix2d[i]
            for char in line:
                arr.append(char)

            i += 1
    guard_pos = find_guard_coord('^', matrix2d)
    guard_pos.append('^')

    start_pos = guard_pos.copy()
    #print(guard_pos)
    matrix_clean = deepcopy(matrix2d)
    guard_path = []
    #guard_path = [[int(guard_pos[0]), int(guard_pos[1]), guard_pos[2]]]
    #matrix2d[int(guard_pos[0])][int(guard_pos[1])] = 'X'

    while(in_boundaries(guard_pos, matrix2d)):

        old_pos = guard_pos.copy()
        guard_pos = move(guard_pos, matrix2d)
        next_pos = calculate_next_pos(guard_pos[2], matrix2d, guard_pos[0], guard_pos[1])
        #print(guard_pos)
        if(in_boundaries(next_pos, matrix2d)):
            matrix2d[int(guard_pos[0])][int(guard_pos[1])] = 'X'
            if not (matrix2d[next_pos[0]][next_pos[1]] == 'X'):
                
                guard_path.append(next_pos)
                count_path+=1
        

    matrix2d[int(old_pos[0])][int(old_pos[1])] = 'X'
    count_path+=1
    for pos in guard_path:
        print(pos)
    print(len(guard_path))
    
    loop_count = 0
    for num, position in enumerate(guard_path):
        new_matrix = matrix_clean.copy()
        new_matrix = place_obstacle(new_matrix, position)

        #print()
        if(loop_detected(new_matrix, position, start_pos)):
        #    print()
        #    for y, line in enumerate(new_matrix):
        #        for x, char in enumerate(line):
        #            if (y == position[0] and x == position[1]):
        #                print('\033[31m'+ char +'\033[0m', end=" ")
        #            else:
        #                print(char, end =" ")
        #        print()
                
            loop_count+=1
            print(num, loop_count)    
    print(loop_count-1)

    

