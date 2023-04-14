import sys
input = sys.stdin.readline
most = [0] *8100
n = int(input())
n_list = []
for i in range(n):
    num = int(input())
    n_list.append(num)
    most[num+4000] +=1

n_list.sort()
s = sum(n_list)
if abs(s%n) > n//2:
    print(s//n+1)
else:
    print(s//n)
print(n_list[n//2])
t = max(most)
tmp = most.index(t)
most.pop(tmp)
if t == max(most):
    tmp = most.index(t)
    print(tmp - 4000+1)
else:
    print(tmp - 4000)

print(max(n_list) - min(n_list))