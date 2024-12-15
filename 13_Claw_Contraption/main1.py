import re



def det(m,n):
 if n==1: return m[0][0]
 z=0
 for r in range(n):
  k=m[:]
  del k[r]
  z+=m[r][0]*(-1)**r*det([p[1:]for p in k],n-1)
 return z



filename = 'input'

 


if __name__ == '__main__':

    slots = []

    with open(filename) as file:
        for line in file:
            if(line.startswith('Button A:')):
                eq1 = re.findall(r'\d+',line)
                eq2 = re.findall(r'\d+',next(file))
                prize = re.findall(r'\d+',next(file))
                
                slots.append([eq1, eq2, prize])
        
        
    count = 0
    for eqs in slots:
        a1, b1, p1, a2, b2, p2 = int(eqs[0][0]), int(eqs[1][0]), int(eqs[2][0]), int(eqs[0][1]), int(eqs[1][1]), int(eqs[2][1])

        print(a1,b1,p1,a2, b2, p2)
        matr = [[a1, b1], [a2,b2]]
        #for line in matr:
        #    print(line)

        matrA = [[p1, b1] ,[p2, b2]]
        matrB = [[a1, p1] ,[a2, p2]]

        d = det(matr, 2)
        dA = det(matrA, 2)
        dB = det(matrB, 2)
        #print(d)

        if(d == 0):
            continue
        x = dA/d
        y = dB/d

        if(x < 0 or x>100 or y < 0 or y > 100):
            continue
        if(x.is_integer() and y.is_integer()):
            count += 3*x + y



        

    
    print(count)
        
