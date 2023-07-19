"""
숫자나 문자가 연속이 아니라면
숫자일 경우 10
문자일 경우 26

2회연속일 경우
10 * 9
3회 연속
10 * 9 * 9
"""

t_list = list(input())
before = None
result = 1
for i in range(len(t_list)):
    if before == t_list[i]:
        if t_list[i] == 'c':
            result = result * 25
        elif t_list[i] == 'd':
            result = result * 9
    else:
        if t_list[i] == 'c':
            result = result * 26
        elif t_list[i] == 'd':
            result = result * 10
    result = result%1000000009
    before = t_list[i]
print(result)