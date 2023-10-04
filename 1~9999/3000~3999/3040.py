n_list = [int(input()) for _ in range(9)]

result = []

def DFS(now, depth, sum_c):
    if depth == 7 and sum_c == 100:
        return True
    for i in range(now+1, 9):
        if n_list[i] + sum_c <=100 :
            result.append(n_list[i])
            t_or_f = DFS(i, depth+1, n_list[i] + sum_c)
            if t_or_f:
                return True
            result.pop()
    return False

for i in range(9):
    result.append(n_list[i])
    t_or_f = DFS(i, 1, n_list[i])
    if t_or_f:
        break
    result.pop()

for i in result:
    print(i)