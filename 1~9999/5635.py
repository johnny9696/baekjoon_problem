n = int(input())
b_list = []
for i in range(n):
    name, date, month, year = map(str,input().split())
    if len(month) == 1:
        month = '0' + month
    if len(date) == 1:
        date = '0' + date
    b_list.append((year, month, date, name))

b_list.sort()

print(b_list[-1][-1])
print(b_list[0][-1])
