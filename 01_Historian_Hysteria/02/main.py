
filename = "input"

def transposeMatrix(m):
    newm = []
    for j in range(0, len(m[0])):
        row = []
        for i in range(0, len(m)): 
            row.append(m[i][j])
        newm.append(row)
    return newm

#from https://www.geeksforgeeks.org/python-program-for-quicksort/
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
    

def count_occurences(l, el):
    count = 0

    for i in range(len(l)):
        if(l[i] == el):
            count += 1
    return count

if __name__ == "__main__":
    #Import input in a 2D array:
    matrix2d = []
    transpose = []
    with open(filename, 'r') as file:
        for line in file:
            matrix2d.append(line.strip().split())

    #transpose the matrix
    transpose = transposeMatrix(matrix2d)
    
    #apply quicksort to both lists
    transpose[0] = quicksort(transpose[0])
    transpose[1] = quicksort(transpose[1])   


    #count occurences of each value and struct it in a dict
    d = {}
    for i in range(len(transpose[0])):
        d[transpose[0][i]] = count_occurences(transpose[1], transpose[0][i])

    #compute similarity score and add up all scores
    sum = 0
    for i in range(len(transpose[0])):
        sum+= int(transpose[0][i])*(d[transpose[0][i]])

    print(sum)