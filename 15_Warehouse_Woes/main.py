import os
import time

filename = "ex1"

def robot_location(warehouse):
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
    else:
        return (0, 0)

def find_last_barrel_plus_one(new_r, new_c, move, warehouse):
    i,j = new_r, new_c
    while(warehouse[i][j] == 'O'):
        (k,h) = get_delta(move)
        i += k
        j += h
    return i, j

def make_move(warehouse, move):

    r,c = robot_location(warehouse)

    dr, dc = get_delta(move)

    new_r = r+dr
    new_c = c+dc 
    
    if(warehouse[new_r][new_c] == '#'):
        return warehouse
    elif(warehouse[new_r][new_c] == '.'):
        warehouse[r][c] = '.'
        warehouse[new_r][new_c] = '@'
        return warehouse
    elif(warehouse[new_r][new_c] == 'O'):
        next_r, next_c = find_last_barrel_plus_one(new_r, new_c, move, warehouse)
        if(warehouse[next_r][next_c] == '.'):
            warehouse[r][c] = '.'
            warehouse[new_r][new_c] = '@'
            warehouse[next_r][next_c] = 'O'
            return warehouse
        elif(warehouse[next_r][next_c] == '#'):
            return warehouse



def score(warehouse):
    count = 0
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == 'O':
                count += 100*i + j
    
    return count

if __name__ == '__main__':
    lines = []
    with open(filename, 'r') as file:  # Use 'r' for reading
        lines = [line.rstrip() for line in file]

    warehouse = []
    moves = "" #string to store all the moves.

    for line in lines:
      if line.startswith(('#', '.', 'O', '@')): #added '[' and ']' to handle doubled input
        warehouse.append(list(line)) #convert each line to a list of chars
      elif line: #if line is not empty
        moves += line 

    
    for move in moves:
        warehouse = make_move(warehouse, move)
        os.system('clear')
        for row in warehouse:
            print(row)
            
            #time.sleep(0.2);
            
            #print(move)

    
    print(score(warehouse))   




