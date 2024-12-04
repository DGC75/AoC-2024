

filename = 'input'

def is_in_boundaries(word, row_pos, col_pos, matrix, rows, cols, orientation):
    if orientation == "cross":
        if row_pos < 1 or row_pos > rows - 2 or col_pos < 1 or col_pos > cols - 2:
            return False
        return True
    
    return True


def cross_check(word, start_pos_x, start_pos_y, matrix, dimx, dimy):
    if(is_in_boundaries(word, start_pos_x, start_pos_y, matrix, dimx, dimy, "cross")):
        center = (start_pos_x, start_pos_y)
        upper_diagonal_start = (center[0]-1, center[1]-1)
        lower_diagonal_start = (center[0]+1, center[1]-1)
        upper_diagonal_word = ""
        lower_diagonal_word = ""
        print(upper_diagonal_start, lower_diagonal_start)
        (i,j) = upper_diagonal_start
        for char in word:
            upper_diagonal_word += matrix[i][j]
            i+=1
            j+=1
        print(upper_diagonal_word)

        (i,j) = lower_diagonal_start
        for char in word:

            lower_diagonal_word += matrix[i][j]
            i-=1
            j+=1
        print(lower_diagonal_word)
        if((lower_diagonal_word == word or lower_diagonal_word[::-1] == word) and (upper_diagonal_word == word or upper_diagonal_word[::-1] == word)):
            return True


if __name__ == '__main__':
    
    #PARAMETERS
    matrix2d = []
    word = "MAS"
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
            if(cross_check(word, i,j, matrix2d, len(matrix2d[0]), len(matrix2d))):
                words_count+=1 



    print(words_count)