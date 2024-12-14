from itertools import groupby

filename = 'input'

def adj_cells(x,y, matr):
    #print('center',x,y)
    up = ['_', (-1, -1)]
    if(x-1>=0 and (x-1< len(matr))):
        up = [matr[x-1][y], (x-1, y)] 
    else:
        up = ['_', (x-1, y)]

    down = ['_', (-1, -1)]
    if (x+1) >=0 and (x+1 < len(matr)): 
        down = [matr[x+1][y], (x+1, y)] 
    else:
        down = ['_', (x+1, y)]

    left = ['_', (-1, -1)]
    if (y-1) >=0 and (y-1 < len(matr[0])):
        left = [matr[x][y-1], (x, y-1)] 
    else:
        left = ['_', (x, y-1)]

    right = ['_', (-1, -1)]
    if (y+1) >=0 and (y+1 < len(matr[0])):
        right = [matr[x][y+1], (x, y+1)]
    else:
        right = ['_', (x, y+1)]



    top_left = ['_', (-1, -1)]
    if(x-1>=0 and (x-1< len(matr)) and (y-1) >=0 and (y-1 < len(matr[0]))):
        top_left = [matr[x-1][y-1], (x-1, y-1)] 
    else:
        top_left = ['_', (x-1, y-1)]
    
    top_right= ['_', (-1, -1)]
    if(x-1>=0 and (x-1< len(matr)) and (y+1) >=0 and (y+1 < len(matr[0]))):
        top_right = [matr[x-1][y+1], (x-1, y+1)] 
    else:
        top_right = ['_', (x-1, y+1)]

    bottom_left = ['_', (-1, -1)]
    if (y-1) >=0 and (y-1 < len(matr[0])) and (x+1) >=0 and (x+1 < len(matr)):
        bottom_left = [matr[x+1][y-1], (x+1, y-1)] 
    else:
        bottom_left = ['_', (x+1, y-1)]

    bottom_right = ['_', (-1, -1)]
    if (y+1) >=0 and (y+1 < len(matr[0])) and (x+1) >=0 and (x+1 < len(matr)):
        bottom_right = [matr[x+1][y+1], (x+1, y+1)] 
    else:
        bottom_right = ['_', (x+1, y+1)]


    
    retval = [top_left, up, top_right, right, bottom_right, down, bottom_left, left]
    #print('retval', retval)
    #retval = [b for b in retval if b]

    
        
    return retval


def adj_cells_2(x,y, matr):
    #print('center',x,y)
    up = []
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



    top_left = []
    if(x-1>=0 and (x-1< len(matr)) and (y-1) >=0 and (y-1 < len(matr[0]))):
        top_left = [matr[x-1][y-1], (x-1, y-1)] 
    
    top_right= []
    if(x-1>=0 and (x-1< len(matr)) and (y+1) >=0 and (y+1 < len(matr[0]))):
        top_right = [matr[x-1][y+1], (x-1, y+1)] 

    bottom_left = []
    if (y-1) >=0 and (y-1 < len(matr[0])) and (x+1) >=0 and (x+1 < len(matr)):
        bottom_left = [matr[x+1][y-1], (x+1, y-1)] 

    bottom_right = []
    if (y+1) >=0 and (y+1 < len(matr[0])) and (x+1) >=0 and (x+1 < len(matr)):
        bottom_right = [matr[x+1][y+1], (x+1, y+1)] 



    
    retval = [up, down, left, right]
    #print('retval', retval)
    retval = [b for b in retval if b]

    
        
    return retval


def figure(input, region):
    adj = [region]
    tmp = [region]
    while(True):
        for r in adj:
            tmp+= adj_cells_2(r[1][0], r[1][1], input)
        tmp = [k for k,v in groupby(sorted(tmp))]
        i = 0
        while(i < len(tmp)):
            if(tmp[i][0] != adj[0][0]):
                tmp.pop(i)
                i-=1
            i+=1
        if adj == tmp:
            break
        adj = tmp.copy()

    return adj


def not_contiguous(char, x, y, regions):

    adj = []
    for region in regions:
        if(region[0] == char):
            adj += figure(input, region)
        
    #adj = [k for k,v in groupby(sorted(adj))]
    #print('adj:', adj)

    if [char, (x,y)] in adj:
        return False

    return True    

def not_in(char, regions):
    if regions == []:
        return True
    else:
        for region in regions:
            if(char == region[0]):
                return False
    return True

def area(input, region):
    
#    adj = [region]
#    tmp = [region]
#    while(True):
#        for r in adj:
#            tmp+= adj_cells(r[1][0], r[1][1], input)
#        tmp = [k for k,v in groupby(sorted(tmp))]
#        i = 0
#        while(i < len(tmp)):
#            if(not tmp[i][0] == adj[0][0]):
#                tmp.pop(i)
#                i-=1
#            i+=1
#        if adj == tmp:
#            break
#        adj = tmp.copy()
#
#    return len(adj)
    area = DFS(region[1][0], region[1][1], input)

    return len(area)


def same_color_adj(cell, input):
    adj = adj_cells_2(cell[1][0],cell[1][1], input)
    
    #print(adj)
    count = 0
    for c in adj:
         if c != []:
            if c[0] == cell[0]:
                count +=1
    
    return count

def perimeter(input, region):


    count = 0
    fig = figure(input, region)
    for cell in fig:
        count += 4 - same_color_adj(cell, input)
        #print(count)
    
    return count

def in_diagonal(adj, i,j,k):
    cell1 = adj[i]
    cell2 = adj[j]
    cell3 = adj[k]

    if((cell1[1][0]+1 == cell2[1][0] and cell1[1][1]-1 == cell2[1][1]) and (cell2[1][0]+1 == cell3[1][0] and cell2[1][1]-1 == cell3[1][1])):
        return True
    
    if((cell3[1][0]+1 == cell2[1][0] and cell3[1][1]+1 == cell2[1][1]) and (cell2[1][0]-1 == cell1[1][0] and cell2[1][1]-1 == cell1[1][1])):
        return True

    return False

def check_angle(adj, i,j,k, region):
    cell1 = adj[i]
    cell2 = adj[j]
    cell3 = adj[k]
    #print(cell1, cell2, cell3)
    if(cell1[0] != region and cell2[0] != region and cell3[0] != region):
        #print(cell1, cell2, cell3, region, "first check")
        if(((cell1[1][0] - 1) == cell2[1][0] == cell3[1][0]) and(cell1[1][1] == cell2[1][1] == cell3[1][1]-1) or #upper left
            (cell1[1][0] == cell2[1][0] == cell3[1][0] - 1) and(cell1[1][1] + 1 == cell2[1][1] == cell3[1][1]) or #upper right
            ((cell1[1][0] + 1) == cell2[1][0] == cell3[1][0]) and(cell1[1][1] == cell2[1][1] == cell3[1][1]+1) or #bottom right
            (cell1[1][0] == cell2[1][0] == cell3[1][0] + 1)and(cell1[1][1] - 1 == cell2[1][1] == cell3[1][1])): #bottom left
            print(cell1, cell2, cell3, region, "angle found")
            return True
            
    return False


def top_left_angle(cell, input, region):
    x = cell[1][0] + 1
    y = cell[1][1] + 1
    

    center = input[x][y]
    left = input[x][y-1]
    opposite = input[x-1][y-1]
    up = input[x-1][y]
    

    if(center == left == up != opposite):
        return 1
    if(center != left and center != up):
        return 1
    
    return 0

def top_right_angle(cell, matr, region):
    x = cell[1][0]+1
    y = cell[1][1]+1

    center = matr[x][y]
    right = matr[x][y+1]
    up = matr[x-1][y]
    opposite = matr[x-1][y+1]

    if(center == right == up != opposite):
        return 1
    if(center != right and center != up):
        return 1
    
    return 0

def bottom_left_angle(cell, input, region):
    x = cell[1][0]+1
    y = cell[1][1]+1
    
    center = input[x][y]
    left = input[x][y-1]
    down = input[x+1][y]
    opposite = input[x+1][y-1]

    if(center == left == down != opposite):
        return 1
    if(center != left and center != down):
        return 1
    
    return 0


def bottom_right_angle(cell, input, region):
    x = cell[1][0]+1
    y = cell[1][1]+1
    
    center = input[x][y]
    right = input[x][y+1]
    opposite = input[x+1][y+1]
    down = input[x+1][y]

    if(center == right == down != opposite):
        return 1
    if(center != right and center != down):
        return 1
    
    return 0


def edges(input, region):
    #edges = #corners, so count corners
    
    area = DFS(region[1][0], region[1][1], input)
    input = make_frame(input)
    count = 0

    
    for cell in area:
        #print(cell)
       
        bottom_right = 0
        bottom_left = 0
        top_right = 0
        top_left = 0
        top_left = top_left_angle(cell, input, region)
        bottom_right = bottom_right_angle(cell, input, region)
        top_right = top_right_angle(cell, input, region)
        bottom_left = bottom_left_angle(cell, input, region)         
        #print(top_left + top_right + bottom_left + bottom_right)
        count += top_left + top_right + bottom_left + bottom_right
        
        
    return count


def make_frame(matr):
    rows = len(input)+2
    cols = len(input[0]) +2
    
    newmatr = [['_']*rows for i in range(cols)]
    
    for i in range(1, len(matr)+1):
        for j in range(1, len(matr[0])+1):
            newmatr[i][j] = matr[i-1][j-1]



    return newmatr

if __name__ == "__main__":

    input = []
    regions = []
    with open(filename) as file:
        for line in file:
            input.append(line.strip())

    for x, line in enumerate(input):
        for y, char in enumerate(line):
            if not_in(char, regions):
                regions += [[char, (x,y)]]
                print(x,y)
            elif(not_contiguous(char, x, y,regions)):
                regions += [[char, (x,y)]]
                print(x,y)


    count = 0


    ROW = len(input)
    COL = len(input[0])
    

    # Initialize direction vectors
    dRow = [0, 1, 0, -1]
    dCol = [-1, 0, 1, 0]
    vis = [[False for i in range(ROW)] for j in range(COL)]

    def isValid(row, col):
        global ROW
        global COL
        global vis
        
        # If cell is out of bounds
        if (row < 0 or col < 0 or row >= ROW or col >= COL):
            return False

        # If the cell is already visited
        if (vis[row][col]):
            return False

        # Otherwise, it can be visited
        return True


    def DFS(row, col, grid):
        global dRow
        global dCol
        global vis

        vis = [[False for i in range(ROW)] for j in range(COL)]

        
        # Initialize a stack of pairs and
        # push the starting cell into it
        st = []
        st.append([row, col])

        # Iterate until the
        # stack is not empty
        count = []
        start_row = row
        start_col = col
        while (len(st) > 0):
            # Pop the top pair
            curr = st[len(st) - 1]
            st.remove(st[len(st) - 1])
            row = curr[0]
            col = curr[1]

            # Check if the current popped
            # cell is a valid cell or not
            if (isValid(row, col) == False):
                continue

            # Mark the current
            # cell as visited
            vis[row][col] = True

            # Print the element at
            # the current top cell
            #print(grid[row][col], end = " ")

            #
            if grid[row][col] == grid[start_row][start_col]:
                count += [[grid[row][col], (row, col)]]
            else:
                continue
            #print(grid[row][col], grid[start_row][start_col])

            # Push all the adjacent cells
            for i in range(4):
                adjx = row + dRow[i]
                adjy = col + dCol[i]
                st.append([adjx, adjy])

        return count




    for region in regions:
        #print('region', region)
        a = area(input, region)
        
        p = edges(input,region)
        print('p', p, 'a', a, region)
        count += p*a

    print(count)

    