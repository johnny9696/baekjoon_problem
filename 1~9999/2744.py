lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = list(lower)
upper = list(upper)

result = ''
text = input()

for i in range(len(text)):
    if text[i] in lower:
        indx =lower.index(text[i])
        result += upper[indx]
    else:
        indx = upper.index(text[i])
        result += lower[indx]
print(result)