T = int(input())

for _ in range(T):
    a,b = map(int,input().split())
    mini = 1
    maxi = 1
    i = 2
    while a != 1 or b != 1:
        div = False
        if a% i == 0 and b%i == 0:
            mini = mini * i
            maxi = maxi * i
            a = a // i
            b = b // i
            div = True
        elif a % i == 0:
            maxi = maxi * i
            a = a // i
            div = True
        elif b % i == 0:
            maxi = maxi * i
            b = b // i
            div = True

        if not div:
            i += 1
    print(maxi,mini)