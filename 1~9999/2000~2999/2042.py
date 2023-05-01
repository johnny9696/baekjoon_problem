import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
tree_height = 0 
length = n
while length !=0:
    length= length //2
    tree_height +=1

tree_size = 2**(tree_height + 1)
start_index =  tree_size//2 - 1
tree = [0] * tree_size

for i in range(start_index+1, start_index+n+1):
    tree[i] =int(input())
    
def setTree(i):
    while i !=1:
        tree[i//2] += tree[i]
        i-=1
setTree(tree_size-1)

def changeVal(index, value):
    diff = value-tree[index]
    while index>0:
        tree[index] = tree[index]+diff
        index = index//2
def getsum(s,e):
    partsum = 0
    while s<=e:
        if s%2 ==1:
            partsum += tree[s]
            s+=1
        if e%2 == 0:
            partsum += tree[e]
            e-=1
        s=s//2
        e=e//2
    return partsum


for _ in range(m+k):
    action,sp, ep = map(int,input().split())
    if action ==1:
        changeVal(sp+start_index, ep)
    else:
        print(getsum(sp+start_index,ep+start_index))