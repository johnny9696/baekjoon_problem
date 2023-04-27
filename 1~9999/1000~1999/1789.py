n = int(input())
s = -1
for i in range(0, n+2):
    s+=i
    if s>=n:
        print(i-1)
        break

