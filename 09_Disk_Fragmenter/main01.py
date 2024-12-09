

filename = 'input'


    
def remove_last_el(new_disk):
    
    #print(new_disk)
    last_el = new_disk[-1]
    #print(last_el)
    if last_el[1] == 0:
        return remove_last_el(new_disk[:-1])
    elif(last_el == ['_', 1]):
        return remove_last_el(new_disk[:-1])
    
    new_disk[-1][1]-=1
    el = new_disk[-1][0]
    if(new_disk[-1][1] == 0):
        new_disk = new_disk[:-1]
    
    

    return new_disk, el

if __name__ == '__main__':
    #parse input

    files = []
    space = []
    line = []
    with open(filename) as file:
        
        for line in file:
            line = line.strip()
            line = list(map(int, line))
            #print(line)
            i = 0
            for char in line:
                if(i % 2 == 0):
                    files.append(char)
                else:
                    space.append(char)
                i+=1

    

    files = list(map(int, files))
    #print('files:', files)
    space = list(map(int, space))
    space.append(0)
    #print('space', space)

    new_disk = []
    for i, file in enumerate(files):
        new_disk.append([i, file])
        while(space[i] > 0):
            new_disk.append(['_', 1])
            space[i]-=1
    for file in new_disk:
        if(file == ['_', 1] and ['_', 1] in new_disk):
            new_disk, el = remove_last_el(new_disk)
            file[0] = el


    i = 0
    len_disk = 0
    for file in new_disk:
        len_disk+=file[1]
    

    disk_string = []
    for list in new_disk:
        while(list[1] > 0):
            disk_string.append(str(list[0]))  
            list[1]-=1
    
    retval = 0
    for id in range(len(disk_string)):
        retval+= id*(int(disk_string[id]))
        #print(id, (int(disk_string[id])))

    print(retval)
