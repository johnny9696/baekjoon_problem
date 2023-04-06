n = int(input())
n_list=[]
for i in range(0, n):
    n_list.append([int(input()),i])
n_list.sort()
max = 0
for i in range(n):
    if max<n_list[i][1]-i:
        max = n_list[i][1] -i

max += 1
print(max)
