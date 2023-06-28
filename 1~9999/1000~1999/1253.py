import sys
input = sys.stdin.readline
n=int(input())
num = list(map(int,input().split()))
num.sort()
result = 0
for k in range(2, n):
    i=0
    j= k-1
    while(i<j):
        if num[k] == num[i]+num[j]:
            if i!=k and j!=k:
                result += 1
                break
            elif i == k:
                 i +=1
            elif j == k:
                j += 1
        elif num[k] > num[i] + num[j]:
            i = i+1
        else:
            j = j-1
print(result)