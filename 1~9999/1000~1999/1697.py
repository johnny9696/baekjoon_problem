import sys
input= sys.stdin.readline
def BFS():
    global n
    global k
    global visited_dict
    depth = 0
    queue= [n-1,n+1,n*2]
    while k not in queue:
        depth +=1
        next_queue =[]
        for i in queue:
            if i not in visited_dict:
                if i>=0 and i<=100000:
                    visited_dict[i] =depth
                    next_queue.append(i-1)
                    next_queue.append(i+1)
                    next_queue.append(i*2)
            else:
                if visited_dict[i] > depth:
                    visited_dict[i]= depth
                    next_queue.append(i - 1)
                    next_queue.append(i + 1)
                    next_queue.append(i * 2)
        queue = next_queue[:]
    return depth


n, k = map(int,input().split())
if n>k:
    n,k=k,n
visited_dict = {n:0}
print(BFS()+1)

