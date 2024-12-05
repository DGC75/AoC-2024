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

def swap(rule, update):
    i, j = 0, 0
    #print(before, after)
    while(j < len(update)):
        if(update[j] == rule[1]):
            i = j+1
            while(i < len(update)):
                if(update[i] == rule[0]):
                    tmp = update[i]
                    update[i] = update[j]
                    update[j] = tmp
                i+=1
 
        j+=1
    return update




def reorder_rules(rules):
    #order by before, at parity, order by after
    rules.sort()
    rules.reverse()
    print(rules)
    return rules

if __name__ == "__main__":
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()] 
    
    rules = []
    updates = []
    rules, updates = parse(lines)
    rules = reorder_rules(rules)
    total = 0
    
    for update in updates:
        tmp_update = []
        is_correct = True
        converged = False
        while(not(converged)):
            tmp_update = update.copy()
            for rule in rules:
                                
                if(comes_after(rule[0], rule[1], update) == True):
                    
                    print("to swap", update)
                    update = swap(rule,update)
                    print("swapped", update)
                    is_correct = False 

            if(tmp_update == update):
                print("converged")
                converged = True 

        if(is_correct == False):
            total += int(update[int(len(update)/2)])
    
    print(total)