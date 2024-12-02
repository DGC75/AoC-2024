



filename = "input"


def list_is_increasing(arr):
    for i in range(len(arr)-1):
        if int(arr[i+1]) - int(arr[i]) <= 0:
            return False
    return True


def list_is_decreasing(arr):
    for i in range(len(arr)-1):
        if int(arr[i+1]) - int(arr[i]) >= 0:
            return False
    return True

def check(arr):

    check = True

    for i in range(len(arr)-1):
        if abs(int(arr[i+1]) - int(arr[i])) > 3:
            check = False
        if not (list_is_increasing(arr) or list_is_decreasing(arr)):
            check = False

    return check

def main():
    sum = 0
    with open(filename) as file:
        for line in file:
            arr = line.strip().split()
            if check(arr) == False:
                for i in range(len(arr)):
                    arr2 = arr.copy()
                    arr2.pop(i)
                    if check(arr2) == True:
                        sum+=1
                        break
            else:
                sum+=1
    print(sum)

main()