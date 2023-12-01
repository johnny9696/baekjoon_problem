h,m,s = map(int,input().split())
needs = int(input())

tmp = s + needs
s = tmp % 60
needs = tmp // 60

tmp = m + needs
m = tmp % 60
needs = tmp // 60

h = (h + needs) % 24
print(h,m,s)