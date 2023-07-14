import sys

input = sys.stdin.readline
r,c,w= map(int,input().split())

#한변의 길이 r+w
#처음과 끝은 1 증간 값은 현재번호 -1, 현재 번호
triangle = [[1 for i in range(j)] for j in range(r+w+1)]
for i in range(3,r+w):
    for j in range(1,i-1):
        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

result = 0
for i in range(r,r+w):
    for j in range(c-1,c+i-r):
        result += triangle[i][j]
print(result)