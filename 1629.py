import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())

def DAC(ta,tb):
    if tb == 1:
        return ta %c

    temp  = DAC(ta,tb//2)

    if tb%2 == 0:
        return temp *temp %c
    else:
        return temp*temp*a%c

print(DAC(a,b))