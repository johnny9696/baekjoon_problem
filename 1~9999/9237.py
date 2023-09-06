"""
크는데 오래 걸리는 걸 먼저 심을 것
다 심고 나서 남은 시간 제거
"""

n = int(input())

n_tree = list(map(int,input().split()))
n_tree.sort(reverse=True)

b_tree = []
for i in range(n):
    b_tree.append(n_tree[i]-(n-i-1))

print(n+max(b_tree)+1)