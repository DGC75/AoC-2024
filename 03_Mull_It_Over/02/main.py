
import re


filename = 'input'



if __name__ == '__main__':
    result = 0
    switch = True
    with open(filename) as file:
        for line in file:
            muls = re.findall(r"mul[(][0-9]+[,][0-9]+[)]|do[(][)]|don[']t[(][)]",line)
            #print(muls)
            for mul in muls:
                if mul == "don't()":
                    switch = False
                if mul == "do()":
                    switch = True
                else:
                    pair = re.findall(r'\d+',mul)
                    if(switch == True):
                        result += int(pair[0])*int(pair[1])
        print(result)
