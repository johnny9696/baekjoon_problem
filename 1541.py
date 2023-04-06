algibra = list(input().split('-'))
result = 0
first = True
for data in algibra:
    if "+" in data:
        tmp_list = list(map(int, data.split('+')))
        tmp = sum(tmp_list)
    else:
        tmp = int(data)
    if first ==True:
        result += tmp
        first = False
    else:
        result += -tmp
print(result)

