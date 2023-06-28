import sys
input = sys.stdin.readline
n = int(input())
fact = [i for i in range(n+1)]
fact[0] = 1

for i in range(1, n+1):
    fact[i] = fact[i-1] * i

act_list = list(map(int,input().split()))
if act_list[0] == 1:
    k = act_list[1]
    visited = [False] * (n+1)
    result = [0] * (n+1)
    for i in range(1, n+1):
        cnt = 1
        for j in range(1,n+1):
            if visited[j]:
                continue
            if k<= cnt*fact[n-i]:
                k -= (cnt-1)*fact[n-i]
                result[i] = j
                visited[i] = True
                break
            cnt +=1
    for i in range(1, n+1):
        print(result[i], end=' ')

else:
    n_list = act_list[1:]
    result = 1
    visited = [False] * (n + 1)
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, act_list[i]):
            if not visited[j]:
                cnt +=1
        result+=cnt*fact[n-i]
        visited[act_list[i]] = True
    print(result)