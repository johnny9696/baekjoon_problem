N = int(input())
n_list = [i for i in range(N+1)]

for i in range(1,N+1):
    j = 1
    while j*j <=i:
        n_list[i] = min(n_list[i],n_list[i-j*j]+1)
        j+=1
print(n_list[-1])