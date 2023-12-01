data = []
i = 1
while len(data) < 1000000:
    n_list = list(str(i))
    if len(n_list)< 2:
        data.append(i)
    else:
        visited = [False] * 10
        is_true = False
        for j in range(0,len(n_list)):
            if visited[int(n_list[j])]:
                is_true = True
                break
            visited[int(n_list[j])] = True
        if not is_true:
            data.append(i)
    i+=1
while True:
    num = int(input())
    if num == 0:
        break
    print(data[num-1])