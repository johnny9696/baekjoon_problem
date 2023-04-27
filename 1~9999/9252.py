import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
text_A = list(input())
text_A.pop()
text_B = list(input())
text_B.pop()
near_list = [[0 for _ in range(len(text_B)+1)] for _ in range(len(text_A)+1)]

for i in range(1,len(text_A)+1):
    for j in range(1,len(text_B)+1):
        if text_A[i-1] == text_B[j-1]:
            near_list[i][j] = near_list[i-1][j-1] + 1
        else:
            near_list[i][j] = max(near_list[i-1][j], near_list[i][j-1])
print(near_list[len(text_A)][len(text_B)])
result = []

def LCS(R,C):
    if R == 0 or C == 0:
        return
    if text_A[R-1] == text_B[C-1]:
        result.append(text_A[R-1])
        LCS(R-1,C-1)
    else:
        if near_list[R-1][C] > near_list[R][C-1]:
            LCS(R-1,C)
        else:
            LCS(R,C-1)

LCS(len(text_A), len(text_B))
for i in range(len(result)-1,-1,-1):
    print(result.pop(), end='')
print()