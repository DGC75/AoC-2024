#from copy import deepcopy
from itertools import groupby
filename = 'input'



def adj_cells(pos, matr):
    up = []
    x = pos[1][0]
    y = pos[1][1]

    if(x-1>=0 and (x-1< len(matr))):
        up = [matr[x-1][y], (x-1, y)] 
    
    down = []
    if (x+1) >=0 and (x+1 < len(matr)): 
        down = [matr[x+1][y], (x+1, y)] 

    left = []
    if (y-1) >=0 and (y-1 < len(matr[0])):
        left = [matr[x][y-1], (x, y-1)] 

    right = []
    if (y+1) >=0 and (y+1 < len(matr[0])):
        right = [matr[x][y+1], (x, y+1)] 
    
    retval = [up, down, left, right]
    retval = [b for b in retval if b]
    #print(retval)

    
        
    return retval


def next_moves(pos, matr):

    #lookup adjacent cells
    adj_cells_arr = adj_cells(pos, matr)
    #print('adj_cells_arr', adj_cells_arr)
    retval = [b for b in adj_cells_arr if (int(matr[pos[1][0]][pos[1][1]]) + 1) == int(b[0])]
    print('retval', retval)
    return retval

def next_moves_arr(current_pos_array, matr):
     
    retval = []
    tmp = current_pos_array
    for pos in tmp:
        tmp = next_moves(pos, matr)
        retval += tmp
        retval = [k for k,v in groupby(sorted(retval))]

    #retval.sort()
    #print(retval)
    return retval

def all_trails_are_finished(arr):
    for el in arr:
        if(el[0] != '9'):
            return False
    return True

def calculate_score(matr, x,y):
     
    trails = 0
    current_pos_array = [[matr[x][y], (x,y)]]

    tmp = next_moves_arr(current_pos_array, matr)
    #print(tmp)
    while(not all_trails_are_finished(tmp)):
        tmp = next_moves_arr(tmp, matr)
        print(tmp)
    
    #print(tmp)
    trails = len(tmp)

            
    return trails
     

if __name__ == '__main__':
    matr = []
    with open(filename) as file:
        for line in file:
            matr.append(line.strip())

    for line in matr:
            print(line)

    scores = 0
    trail = 0
    for x, line in enumerate(matr):
        for y, char in enumerate(line):
            if(char == '0'):
                
                score = calculate_score(matr, x,y)
                scores += score
                print('trail',trail)
                print('score', score)
                trail+=1
    
    print(scores)