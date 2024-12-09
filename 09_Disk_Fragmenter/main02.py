

filename = 'input'


def compact_spaces(new_disk):
    i = 0
    j = i + 1
    #print('before compact', new_disk)
    while(j < len(new_disk)):
        if(new_disk[i][0] == '_' and new_disk[j][0] == '_'):
            #print(new_disk[i], new_disk[j])
            tmp = ['_', new_disk[i][1] + new_disk[j][1]]
            new_disk.pop(i)
            new_disk.pop(i)
            new_disk.insert(i, tmp)
        i+=1
        j = i + 1
    #print('after compact', new_disk)
    return new_disk

def insert_in_leftmost_space(file, new_disk):
    index_of_old_file = new_disk.index(file)
    for i, space in enumerate(new_disk):
            
        #print(index_of_old_file)
        if(space[0] == '_' and file[1] <= space[1] and i < index_of_old_file):
            #print('space found at index', i, 'for block', file, file[1] ,'<=', space[1])
            
            #print('index of old file:', index_of_old_file, file)
            new_disk[index_of_old_file][0] = '_' #cancella vecchio file rimpiazzandolo con degli spazi
            remaining_space = space[1] - file[1]
            new_disk.pop(i) #rimuovi spazio necessario all'allocazione
            #print('index of old file:', index_of_old_file, file)
            #print(file)
            new_disk.insert(i, file) #inserisci file
            new_disk.insert(i+1, ['_', remaining_space]) #inserisci spazio rimanente
            

            
            new_disk = compact_spaces(new_disk)
            #print(new_disk)
            break

    return new_disk

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
        new_disk.append(['_', space[i]])

    

    #        new_disk, el = remove_last_el(new_disk)
    #        file[0] = el
    

    for file in reversed(new_disk):
        if(file[0] != '_'):
            print(file)
            new_disk = insert_in_leftmost_space(file.copy(), new_disk)

    #for i, file in enumerate(new_disk):
    #    if(file == ['_', 0]):
    #        new_disk.remove(file)

    for file in new_disk:
        if(file == ['_', 0]):
            new_disk.remove(file)

    print(new_disk)


    disk_string = []
    for list in new_disk:
        while(list[1] > 0):
            disk_string.append(str(list[0]))  
            list[1]-=1
    print(disk_string)
    retval = 0

    
    #print(new_disk)
    for id in range(len(disk_string)):
        if(disk_string[id] == '_'):
            continue
        retval+= id*(int(disk_string[id]))
        print(id, (int(disk_string[id])))

    print(retval)
