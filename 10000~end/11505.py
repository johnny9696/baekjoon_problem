import sys
input = sys.stdin.readline
div_num = 1000000007
n,m,k = map(int,input().split())
tmp = n
count = 1
while tmp!=0:
    tmp = tmp // 2
    count += 1

length = 2**count + 1
tree = [1] * length
start_index = length // 2 -1
#initialize tree
for i in range(start_index+1,start_index+n+1):
    tree[i] = int(input())
#set tree
for i in range(start_index,0,-1):
    tree[i] = tree[2*i]*tree[2*i+1]%div_num

def multi_tree(sp,ep):
    multi = 1
    while sp<=ep:
        if sp %2 ==1:
            multi = multi * tree[sp]
            sp +=1
        if ep %2 == 0:
            multi = multi * tree[ep]
            ep -=1
        sp = sp//2
        ep = ep//2
    return multi


for _ in range(m+k):
    action, sp, ep = map(int,input().split())
    if action == 1 :
        sp = sp + start_index
        tree[sp] = ep
        while sp != 0 :
            if sp %2 == 0:
                tree[sp//2] = tree[sp]*tree[sp-1]
            else:
                tree[sp//2] = tree[sp]*tree[sp+1]
            sp = sp//2
    else:
        print(multi_tree(sp,ep)%div_num)