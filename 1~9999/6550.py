import sys

input = sys.stdin.readline

while True:
    try:
        a,b = map(str, input().split())
    except:
        break
    a = list(a)
    b= list(b)
    length  = len(a)
    s_num = 0

    for now in b:
        if now == a[s_num]:
            s_num += 1
        if s_num == length:
            break
    if s_num == length:
        print('Yes')
    else:
        print('No')