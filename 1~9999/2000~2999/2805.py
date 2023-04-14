import sys
input = sys.stdin.readline

n, m = map(int,input().split())
wood = list(map(int,input().split()))
wood.append(0)
wood.sort()

result = sum(wood)
t = 0
n += 1
for i in wood:
    result -= (i-t)*n
    t = i
    if result <= m:

        break
    n -= 1

if result == m:
    print(t)
else:
    if (m-result)%n !=0:
        print(t-((m-result)//n +1))
    else:
        print(t-(m-result)//n)


