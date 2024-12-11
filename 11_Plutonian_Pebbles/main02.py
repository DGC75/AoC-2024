from collections import Counter

filename = 'input'

def transform(l):
    retval = []
    for el in l:
          retval.append(list(el))

    return retval      

def update(l):
     
    i = 0
    tmp = []
    while(i < len(l)):
        els =process_element(l[i])
        if(isinstance(els[0], list)):
            for x in els:
                tmp.append(x)
        else:
            tmp.append(els)
        i+=1
         
    return tmp

def process_element(input):

        if(input[0] == 0):
            return [input[0]+1, input[1]]
            
        elif(len(str(input[0])) % 2 == 0):
            s = str(input[0])
            firstpart, secondpart = s[:len(s)//2], s[len(s)//2:]
            return [[int(firstpart), input[1]], [int(secondpart), input[1]]]
        else:
            return [input[0]*2024, input[1]]

def compact_list(l):
    
    l.sort()
    i = 0
    j = i + 1
    while(j < len(l)):
        if(l[i][0] == l[j][0]):
            
            x = l.pop(i)
            y = l.pop(i)
            tmp = [x[0], x[1] + y[1]]
            
            
            l.insert(i, tmp)
            i = 0
            j = 1

        i+= 1
        j = i + 1
    return l


if __name__ == '__main__':

    input =[]

    with open(filename) as file:
        for line in file:
            input = line.strip().split(' ')


    input = list(map(int, input))

    counter = list(Counter(input).items())

    counter = transform(counter)

    i = 0

    print(counter)
    while(i < 75):
         
        #remove element and substitute with appropriate ones:
        counter = update(counter)
        counter = compact_list(counter)
        i+=1
    

    def sum_counter(l):
        retval = 0
        for el in l:
            retval += el[1]
        return retval

    print(sum_counter(counter))