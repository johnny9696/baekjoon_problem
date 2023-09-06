n = int(input())
sim_fibo = [1,1,1,1]
for i in range(4, n+1):
    sim_fibo.append(sim_fibo[i-1] + sim_fibo[i-3])
print(sim_fibo[n])