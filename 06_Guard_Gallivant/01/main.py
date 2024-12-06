


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

if __name__ == "__main__":
    matrix2d = []

    count_path = 1

    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
        i = 0
        for line in lines:
            matrix2d.append([])
            arr = matrix2d[i]
            for char in line:
                arr.append(char)

            i += 1
    #for line in matrix2d:
    #    print(line)
    guard_pos = find_guard_coord('^', matrix2d)
    guard_pos.append('^')
    print(guard_pos)

    while(in_boundaries(guard_pos, matrix2d)):

        old_pos = guard_pos.copy()
        guard_pos = move(guard_pos, matrix2d)
        next_pos = calculate_next_pos(guard_pos[2], matrix2d, guard_pos[0], guard_pos[1])
        print(guard_pos)
        if(in_boundaries(next_pos, matrix2d)):
            matrix2d[int(guard_pos[0])][int(guard_pos[1])] = 'X'
            if not (matrix2d[next_pos[0]][next_pos[1]] == 'X'):
                count_path+=1
        #for line in matrix2d:
        #    print(line)


    print(count_path)

