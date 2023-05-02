import sys
input = sys.stdin.readline

node, question = map(int,input().split())
length = node
count = 0
while node!=0:
    node = node // 2
    count+=1
count +=1
full_list = [sys.maxsize] * ((2**count)+1)
start_index = len(full_list)// 2 - 1

for i in range(1, length+1):
    full_list[start_index+i] = int(input())

for i in range(start_index,0,-1):
    full_list[i] = min(full_list[2*i],full_list[2*i+1])

def min_Tree(s,e):
    Min = sys.maxsize
    while s<=e:
        if s%2 == 1:
            Min = min(Min, full_list[s])
            s+=1
        if e %2 == 0:
            Min = min(Min, full_list[e])
            e-=1
        s=s//2
        e=e//2
    return Min

for _ in range(question):
    s,e = map(int,input().split())
    print(min_Tree(start_index+s,start_index+e))