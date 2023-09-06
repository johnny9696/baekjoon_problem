"""
t(0)=1
t(1)=t(0)*t(0)=1
t(2)=t(0)*t(1)+t(1)*t(0)=2
t(3)=t(0)*t(2)+t(1)*t(1)+t(2)*t(0)=5
t(4) = 14
t(5) = 28 + 10 + 4
"""
n = int(input())
n_list=[0] * (n+1)
n_list[0] = 1

for i in range(1, n+1):
    for j in range(0,i):
        n_list[i] += (n_list[j] * n_list[i-j-1])
print(n_list[n])

