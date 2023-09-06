n= int(input())
n_list=list(map(int,input().split()))
stack = []
result=[0]*n

for i in range(len(n_list)):
    while stack and n_list[stack[-1]]<n_list[i]:
        result[stack.pop()] = str(n_list[i])
    stack.append(i)
while stack:
     result[stack.pop()] = str(-1)

print(result)