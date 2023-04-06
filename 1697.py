def BFS(n,k):
    global visited
    depth = 0
    visited.append((n))
    depth_dict=dict({0:[n]})
    while True:
        t_list = depth_dict[depth]
        n_list =[]
        depth += 1
        for t in t_list:
            a = t - 1
            b = t + 1
            c = t * 2
            if a == k or b == k or c ==k:
                print(depth_dict)
                return depth
            if a not in visited and a>=0 and a<=100000:
                visited.append(a)
                n_list.append(a)
            if b not in visited and b>=0 and b<=100000:
                visited.append(b)
                n_list.append(b)
            if c not in visited and c>=0 and c<=100000:
                visited.append(c)
                n_list.append(c)
        depth_dict[depth] = n_lis]

n,k = map(int,input().split())
visited = []
if n<k:
    print(BFS(n,k))
else:
    print(n-k)
