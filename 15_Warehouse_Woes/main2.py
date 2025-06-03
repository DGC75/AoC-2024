import os
import time

filename = "input"

def find_robot_location(warehouse):
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == '@':
                return (i,j)

def get_delta(direction):
    if direction == '^':
        return (-1, 0)
    elif direction == 'v':
        return (1, 0)
    elif direction == '<':
        return (0, -1)
    elif direction == '>':
        return (0, 1)


def move_barrels_horizontally(move, warehouse, robot_location):
    i,j = robot_location
    dr, dc = get_delta(move)

    start_r = i + dr
    start_c = j + dc

    i += dr
    j += dc
    while(warehouse[i][j] == '[' or warehouse[i][j] == ']'):
        i+= dr
        j+= dc
    
    if(warehouse[i][j] == '.'):
        tmp ='.'
        curr_cell = '.'
        while((start_r, start_c) != (i+dr,j+dc)):
            curr_cell = warehouse[start_r][start_c]
            warehouse[start_r][start_c] = tmp
            tmp = curr_cell

            start_r+= dr
            start_c+= dc

        return warehouse

    return warehouse


def get_root_position(warehouse, move, robot_location):
    r,c = robot_location
    dr, dc = get_delta(move)

    if(warehouse[r+dr][c+dc] == '['):
        return (r+dr, c+dc)
    elif(warehouse[r+dr][c+dc-1] == '['):
        return (r+dr, c+dc-1)

    raise Exception('Invalid root position')

def there_is_free_space(root_position, move, warehouse):


    r,c = root_position
    dr, dc = get_delta(move)

    if(warehouse[r+dr][c+dc] == '.' and warehouse[r+dr][c+dc+1] == '.'):
        return True
    
    return False

def move_barrel_vertically(warehouse, root_position, move):

    r,c = root_position
    dr, dc = get_delta(move)

    if(warehouse[r+dr][c+dc] == '.' and warehouse[r+dr][c+dc+1] == '.'):
        warehouse[r+dr][c+dc] = '[' 
        warehouse[r+dr][c+dc+1] = ']'

        warehouse[r][c] = '.' 
        warehouse[r][c+1] = '.'
        return warehouse
    

    raise Exception("You shouldnt be here")
               
def block_fill(move, warehouse, barrels_set):

    for barrel in barrels_set.copy():
        dr, dc = get_delta(move)
        left = warehouse[barrel[0][0]+dr][barrel[0][1]+dc]
        right = warehouse[barrel[1][0]+dr][barrel[1][1]+dc]

        left_coord = (barrel[0][0]+dr,barrel[0][1]+dc)
        right_coord = (barrel[1][0]+dr,barrel[1][1]+dc)

        barrel_coord = (left_coord, right_coord)


        if left == '[' and right == ']' and barrel_coord not in barrels_set:
            barrels_set.add(barrel_coord)
            barrels_set = barrels_set | block_fill(move, warehouse, barrels_set)
        

        if left == ']':
            barrel_coord = ((left_coord[0], left_coord[1]-1),left_coord)
            if barrel_coord not in barrels_set:
                barrels_set.add(barrel_coord)
                barrels_set = barrels_set | block_fill(move, warehouse, barrels_set)


        if right == '[':
            barrel_coord = (right_coord, (right_coord[0], right_coord[1]+1))
            if barrel_coord not in barrels_set:
                barrels_set.add(barrel_coord)
                barrels_set = barrels_set | block_fill(move, warehouse, barrels_set)


    return barrels_set


def is_blocked(warehouse, block, move):
    dr, dc = get_delta(move)
    

    for cell in block:
        r,c = cell[0], cell[1]
        if warehouse[r+dr][c+dc] == '#':
            return True
        

    return False


def move_area_vertically(warehouse, area_to_move):
    
    for block in area_to_move:
        for cell in block:
            warehouse[cell[0]][cell[1]] = '.'

    dr, dc = get_delta(move)

    for block in area_to_move:
        warehouse[block[0][0]+dr][block[0][1]+dc] = '[' 
        warehouse[block[1][0]+dr][block[1][1]+dc] = ']' 

def move_block_of_barrels_vertically(move, warehouse, robot_location):

    r,c = robot_location
    dr, dc = get_delta(move)    

    new_r, new_c = r+dr, c+dc
    barrel = None

    if warehouse[new_r][new_c] == '[':
        barrel = ((new_r, new_c),(new_r, new_c+1))
    elif warehouse[new_r][new_c] == ']':
        barrel = ((new_r, new_c-1),(new_r, new_c))

    barrels_set = {barrel}

    area_to_move = block_fill(move, warehouse, barrels_set)


    for block in area_to_move:
        if is_blocked(warehouse, block, move):
            return warehouse
    
    
    move_area_vertically(warehouse, area_to_move)

    return warehouse

def make_move(warehouse, move):

    robot_location = find_robot_location(warehouse)

    dr, dc = get_delta(move)

    new_r = robot_location[0]+dr
    new_c = robot_location[1]+dc 

    if((move == '>' or move == '<') and (warehouse[new_r][new_c]== '[' or warehouse[new_r][new_c]== ']')):
        warehouse = move_barrels_horizontally(move, warehouse, robot_location)
    elif((move == '^' or move == 'v') and (warehouse[new_r][new_c]== '[' or warehouse[new_r][new_c]== ']' )): #move == v or ^
        warehouse = move_block_of_barrels_vertically(move, warehouse, robot_location)

    if(warehouse[new_r][new_c] == '.'):
        warehouse[robot_location[0]][robot_location[1]] = '.'
        warehouse[new_r][new_c] = '@'




    return warehouse

def score(warehouse):
    count = 0
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == '[':
                count += 100*i + j

    
    return count

def double_warehouse(warehouse):
    big_warehouse = []
    for row in warehouse:
        big_row = []
        for cell in row:
            if cell == '#':
                big_row.extend(['#', '#'])
            elif cell == 'O':
                big_row.extend(['[', ']'])
            elif cell == '.':
                big_row.extend(['.', '.'])
            elif cell == '@':
                big_row.extend(['@', '.'])
        big_warehouse.append(big_row)
    return big_warehouse


if __name__ == '__main__':
    lines = []
    with open(filename, 'r') as file:  # Use 'r' for reading
        lines = [line.rstrip('\n') for line in file]

    warehouse = []
    moves = "" #string to store all the moves.

    for line in lines:
      if line.startswith(('#', '.', 'O', '@')): #added '[' and ']' to handle doubled input
        warehouse.append(list(line)) #convert each line to a list of chars
      elif line: #if line is not empty
        moves += line 


    warehouse = double_warehouse(warehouse)
    
    for move in moves:

        #for row in warehouse:
        #    print(''.join(row))
        #print(move)  


        warehouse = make_move(warehouse, move)
        #os.system('clear')
        
  
        #time.sleep(1)
            
            #print(move)

    for row in warehouse:
        print(''.join(row)) 
    print(score(warehouse))   




