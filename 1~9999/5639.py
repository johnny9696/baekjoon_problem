import sys
sys.setrecursionlimit(10**6)
num_list =[]
while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break

def postorder(s,e):
    if s>e:
        return
    mid = e +1
    for i in range(s+1,e+1):
        if num_list[s] <num_list[i]:
            mid = i
            break
    postorder(s+1,mid-1)
    postorder(mid,e)
    print(num_list[s])

postorder(0,len(num_list)-1)
