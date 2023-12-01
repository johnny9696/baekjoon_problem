"""
햇빛 1 온기 +1
햇빛 10 수분 -1
물 1 수분 +1
물 10 온기 -1
온기 수분은 0이하가 되지 않음
큰걸 먼저 다 체우고 작은걸 다 체우면 되나?
"""

n_num = list(map(int,input().split()))
x = max(n_num)
y = min(n_num)
result = x + y//10 + y

print(result)