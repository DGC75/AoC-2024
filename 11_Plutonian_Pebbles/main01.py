
filename = 'input'



if __name__ == '__main__':

    input =[]

    with open(filename) as file:
        for line in file:
            input = line.strip().split(' ')


    input = list(map(int, input))

    #process input
    for x in range(25):
        print('blink', x+1)
        i = 0
        while(i < len(input)):
            if(input[i] == 0):
                num = input.pop(i)
                input.insert(i, num+1)
                
            elif(len(str(input[i])) % 2 == 0):
                s = str(input.pop(i))
                firstpart, secondpart = s[:len(s)//2], s[len(s)//2:]
                #print(firstpart, secondpart)
                input.insert(i, int(secondpart))
                input.insert(i, int(firstpart))
                i+=1
            else:
                num = input.pop(i)
                input.insert(i, num*2024)
                
            i+=1
        print(input)


    print(len(input))