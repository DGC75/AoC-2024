



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



def main():
    sum = 0
    check = True
    with open(filename) as file:
        for line in file:
            check = True
            arr = line.strip().split()
            for i in range(len(arr)-1):
                if abs(int(arr[i+1]) - int(arr[i])) > 3:
                    check = False
                if not (list_is_increasing(arr) or list_is_decreasing(arr)):
                    check = False
            
            if check == True:
                sum+=1
    print(sum)

main()