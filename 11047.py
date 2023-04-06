import sys
input = sys.stdin.readline
def find_min(c_coin,remain):
    result =[]
    count = remain//c_coin[-1]
    remain = remain%c_coin[-1]
    if remain == 0:
        return count
    else:
        t = find_min(c_coin[:-1], remain)
        if t != None:
            result.append(t)
    if not result :
        return None
    min_result = min(result)
    count += min_result
    return count




n, k = map(int,input().split())
coin =[]
for _ in range(n):
    coin.append(int(input()))

print(find_min(coin,k))