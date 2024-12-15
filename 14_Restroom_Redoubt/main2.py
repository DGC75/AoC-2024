import re
import os
import time

filename = 'input'

def detect_tree(position):

    for row in position:
        for cell in row:
            if(cell > 1):
                    return False

    return True

if __name__ == '__main__':

    robots = []

    with open(filename) as file:
        for line in file:
            robot = re.findall(r'[-+]?[0-9]+',line)
            robots.append([[int(robot[0]), int(robot[1])], [int(robot[2]), int(robot[3])]])
        

    for robot in robots:
        print(robot)

    k = 0
    while(True):
        os.system('clear')
        seconds = k

        wide = 101
        tall = 103

        positions = [ [0]*wide for i in range(tall)]

        for robot in robots:
            px = robot[0][0]
            py = robot[0][1]
            vx = robot[1][0]
            vy = robot[1][1]

            final_pos = [(px+ vx*seconds)%wide,(py+ vy*seconds)%tall]
            coord = [final_pos[1], final_pos[0]]

            positions[coord[0]][coord[1]]+=1

        for line in positions:
            print(line)
        print('seconds:', k)
        #time.sleep(1)
        if(detect_tree(positions)):
            break
        k+=1


    coord1 =[0,0]
    coord2 =[0, (wide-1)//2 + 1]
    coord3 =[(tall-1)//2 + 1, 0]
    coord4 =[(tall-1)//2 + 1, (wide-1)//2 + 1]

    coords = [coord1, coord2, coord3, coord4]
    print(coords)
    tall = (tall-1)//2 
    wide = (wide-1)//2

    answer = 1
    for coord in coords:
        count = 0
        i,j = coord[0], coord[1]
        while(i < coord[0]+tall):
            j = coord[1]
            while(j < coord[1]+ wide):
                #print(i,j, positions[i][j])
                count+= positions[i][j]
                j+=1
            i+=1
            
        print(count)
        answer*= count

    print(answer)