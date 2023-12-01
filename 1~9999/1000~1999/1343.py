x_list = list(input())

result = []
cnt = 0
for i in x_list:
    if i == 'X':
        cnt += 1
    else:
        result.append(cnt)
        result.append(i)
        cnt = 0
if cnt != 0:
    result.append(cnt)

p_result = ''
for i in result:
    if i != '.':
        while i >0:
            if i >=4:
                p_result += 'AAAA'
                i += -4
            elif i >= 2:
                p_result += 'BB'
                i += -2
            else:
                p_result = -1
                break
    else:
        p_result += i
    if p_result == -1:
        break

print(p_result)