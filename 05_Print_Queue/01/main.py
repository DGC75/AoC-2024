import re

filename = "input"


def parse(lines):
    i = 0
    while(i < len(lines)):
        
        if(lines[i] == ''):
            i+=1
            break
        rules.append(re.split(r'[|]', lines[i]))
        
        i+=1
        
    while(i < len(lines)):
        updates.append(re.split(r'[,]', lines[i]))
        i+=1
        
    return rules, updates
            
def comes_after(before, after, list):
    i, j = 0, 0
    #print(before, after)
    while(j < len(list)):
        if(list[j] == after):
            i = j+1
            while(i < len(list)):
                if(list[i] == before):
                    return True
                i+=1
 
        j+=1
    return False

if __name__ == "__main__":
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()] 
    
    rules = []
    updates = []
    rules, updates = parse(lines)
    total = 0
    for update in updates:
        is_correct = True
        for rule in rules:
            if(comes_after(rule[0], rule[1], update) == True):
                print('after', update)
                is_correct = False
                break
        if(is_correct):
            total += int(update[int(len(update)/2)])
    
    print(total)