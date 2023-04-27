"""
1 : 3
2 : 7
3 : 17
4 : 41
n-1 * 2 + n-2
"""
n  = int(input())
result = [1] *(n+1)
result[1] = 3
div =9901
for i in range(2, n+1):
    result[i] = (result[i-1]*2 + result[i-2])%div
print(result[n])