"""
blr
lbr
lrb
"""
import sys
input = sys.stdin.readline

class b_tree():
    def __init__(self, left =None, right = None):
        self.left = left
        self.right = right


node = int(input())
p_tree= dict()
for _ in range(node):
    p, l, r= input().split()
    p_tree[p] = b_tree(l,r)

result_BLR = []
result_LBR = []
result_LRB = []

def DFS(root):
    result_BLR.append(root)
    l_next= p_tree[root].left
    r_next=p_tree[root].right
    if l_next !='.':
        DFS(l_next)
    result_LBR.append(root)
    if r_next !='.':
        DFS(r_next)
    result_LRB.append(root)

DFS('A')
print(''.join(result_BLR))
print(''.join(result_LBR))
print(''.join(result_LRB))



