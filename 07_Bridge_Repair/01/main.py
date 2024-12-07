import re

filename = 'input'

split_list = lambda lst: (lst[-1], lst[:-1])
ops = ['+', '*']

def process_eq(eq):
    retval = []
    if(len(eq) <= 1):
        return eq
    head, tail = split_list(eq)
    #print(head, tail)
    tail = process_eq(tail)
    for el in tail:
        for op in ops:
            if(op == '+'):
                retval.append(head + el)
            if(op == '*'):
                retval.append(head * el)    
    #print(retval)
    return retval
    
if __name__ == '__main__':
    #parse input
    input = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            line = re.split(r'[: ]', line)
            line.remove('')
            for i, num in enumerate(line):
                line[i] = int(num)
            input.append(line)

    #process input
    print(input)
    
    retval = 0
    for equation in input:
        result = equation[0]
        if result in process_eq(equation[1:]):
            retval += result


    print(retval)