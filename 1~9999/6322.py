import math

case = 1
while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and  c == 0:
        break
    print('Triangle #{}'.format(case))
    if a == -1:
        ta = c ** 2 - b ** 2
        if ta > 0:
            ta = math.sqrt(ta)
            print('a = {:.3f}'.format(ta))
        else:
            print('Impossible.')
    elif b == -1:
        tb = c ** 2 - a ** 2
        if tb >0 :
            tb = math.sqrt(tb)
            print('b = {:.3f}'.format(tb))
        else:
            print('Impossible.')
    elif c == -1:
        tc = a ** 2 + b ** 2
        if tc >0 :
            print('c = {:.3f}'.format(math.sqrt(tc)))
        else:
            print('Impossible.')
    print()
    case += 1
