
import re


filename = 'input'









if __name__ == '__main__':
    result = 0
    with open(filename) as file:
        for line in file:
            muls = re.findall(r"mul[(][0-9]+[,][0-9]+[)]",line)
            #print(muls)
            for mul in muls:
                pair = re.findall(r'\d+',mul)
                result += int(pair[0])*int(pair[1])
        print(result)