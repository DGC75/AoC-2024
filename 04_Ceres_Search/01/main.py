

filename = 'input'

def is_in_boundaries(word, row_pos, col_pos, matrix, rows, cols, orientation):
    if orientation == "horizontal":
        if col_pos + len(word) > cols:
            return False
        return True
    if orientation == "vertical":
        if row_pos + len(word) > rows:
            return False
        return True
    if orientation == "diagonal_clockwise":
        if row_pos + len(word) > rows or col_pos + len(word) > cols:
            return False
        return True
    if orientation == "diagonal_counterclockwise":
        if row_pos + len(word) > rows or col_pos - len(word) + 1 < 0:
            return False
        return True
    if orientation == "horizontal_backward":
        if col_pos - len(word) + 1 < 0:
            return False
        return True
    if orientation == "vertical_backward":
        if row_pos - len(word) + 1 < 0:
            return False
        return True
    if orientation == "diagonal_clockwise_backward":
        if row_pos - len(word) + 1 < 0 or col_pos - len(word) + 1 < 0:
            return False
        return True
    if orientation == "diagonal_counterclockwise_backward":
        if row_pos - len(word) + 1 < 0 or col_pos + len(word) > cols:
            return False
        return True


def check_horizontal(word, start_pos_x, start_pos_y, matrix, dimx, dimy):
    
    if(is_in_boundaries(word, start_pos_x, start_pos_y, matrix, dimx, dimy, "horizontal")):
        i = start_pos_y
        for char in word:
            if char != matrix[start_pos_x][i]:
                
                return False
            i+=1
        return True



def    check_vertical(word, start_pos_x, start_pos_y, matrix, dimx, dimy):
    if(is_in_boundaries(word, start_pos_x, start_pos_y, matrix, dimx, dimy, "vertical")):
        i = start_pos_x
        for char in word:
            if char != matrix[i][start_pos_y]:
                
                return False
            i+=1
        return True

def    check_diagonal_clockwise(word, start_pos_x, start_pos_y, matrix, dimx, dimy):
    if(is_in_boundaries(word, start_pos_x, start_pos_y, matrix, dimx, dimy, "diagonal_clockwise")):
        i = start_pos_x
        j = start_pos_y
        for char in word:
            if char != matrix[i][j]:
                
                return False
            i+=1
            j+=1
        return True

def    check_diagonal_counterclockwise(word, start_pos_x, start_pos_y, matrix, dimx, dimy):
    if(is_in_boundaries(word, start_pos_x, start_pos_y, matrix, dimx, dimy, "diagonal_counterclockwise")):
        i = start_pos_x
        j = start_pos_y
        for char in word:
            if char != matrix[i][j]:
                
                return False
            i+=1
            j-=1
        return True

def    check_horizontal_backward(word, start_pos_x, start_pos_y, matrix, dimx, dimy):
    
    if(is_in_boundaries(word, start_pos_x, start_pos_y, matrix, dimx, dimy, "horizontal_backward")):
        i = start_pos_y
        for char in word:
            if char != matrix[start_pos_x][i]:
                return False
            i-=1
        return True

def    check_vertical_backward(word, start_pos_x, start_pos_y, matrix, dimx, dimy):
    if(is_in_boundaries(word, start_pos_x, start_pos_y, matrix, dimx, dimy, "vertical_backward")):
        i = start_pos_x
        for char in word:
            if char != matrix[i][start_pos_y]:
                return False
            i-=1
        return True


def    check_diagonal_clockwise_backward(word, start_pos_x, start_pos_y, matrix, dimx, dimy):
    if(is_in_boundaries(word, start_pos_x, start_pos_y, matrix, dimx, dimy, "diagonal_clockwise_backward")):
        i = start_pos_x
        j = start_pos_y
        for char in word:
            if char != matrix[i][j]:
                return False
            i-=1
            j-=1
        return True

def    check_diagonal_counterclockwise_backward(word, start_pos_x, start_pos_y, matrix, dimx, dimy):
    if(is_in_boundaries(word, start_pos_x, start_pos_y, matrix, dimx, dimy, "diagonal_counterclockwise_backward")):
        i = start_pos_x
        j = start_pos_y
        for char in word:
            if char != matrix[i][j]:
                
                return False
            i-=1
            j+=1
        return True



#def    check_diagonal_clockwise_backward(start_pos_x, start_pos_y, matrix, dimx, dimy)
#def    check_diagonal_counterclockwise_backward(start_pos_x, start_pos_y, matrix, dimx, dimy)


if __name__ == '__main__':
    
    #PARAMETERS
    matrix2d = []
    word = 'XMAS'
    words_count = 0

    #LOAD MATRIX
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
        i = 0
        for line in lines:
            matrix2d.append([])
            arr = matrix2d[i]
            for char in line:
                arr.append(char)

            i += 1
    
    #SEARCH
    i = 0
    j = 0
    for i in range(len(matrix2d[0])):
        for j in range(len(matrix2d)):
            print(i,j)
            if(check_horizontal(word, i,j, matrix2d, len(matrix2d[0]), len(matrix2d))):
                print("horizontal")
                words_count+=1
            if(check_vertical(word, i,j, matrix2d, len(matrix2d[0]), len(matrix2d))):
                print("vertical")
                words_count+=1
            if(check_diagonal_clockwise(word, i,j, matrix2d, len(matrix2d[0]), len(matrix2d))):
                print("diagonal_clockwise")
                words_count+=1 
            if(check_diagonal_counterclockwise(word, i,j, matrix2d, len(matrix2d[0]), len(matrix2d))):
                print("diagonal_counterclockwise")
                words_count+=1   
            if(check_horizontal_backward(word, i,j, matrix2d, len(matrix2d[0]), len(matrix2d))):
                print("horizontal_backward")
                words_count+=1 
            if(check_vertical_backward(word, i,j, matrix2d, len(matrix2d[0]), len(matrix2d))):
                print("vertical_backward")
                words_count+=1 
            if(check_diagonal_clockwise_backward(word, i,j, matrix2d, len(matrix2d[0]), len(matrix2d))):
                print("diagonal_clockwise_backward")
                words_count+=1 
            if(check_diagonal_counterclockwise_backward(word, i,j, matrix2d, len(matrix2d[0]), len(matrix2d))):
                print("check_diagonal_counterclockwise_backward")
                words_count+=1  



    print(words_count)