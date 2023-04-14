import sys
"""
문자열이 짝수인 경우 같은 문자가 짝수개
문자열이 홀수인경우 한문자는 1개의 문자 나머지는 짝수

갯수의 절반만큼만 추가 해서 끝을 찍고
거꾸로 옴
"""
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = list(alpha)
text = list(input())
c_alpha = [0]*26
#짝수 인경우 True, 홀수 인 경우 False
if len(text) %2 == 1:
    Even_Odd = False
else:
    Even_Odd = True
for i in text:
    c_alpha[alpha.index(i)] +=1
result=''
odd = None
make = True
for c, i in enumerate(c_alpha):
    if i%2 == 1:
        if odd != None:
            make = False
            break
        if Even_Odd:
            make = False
            break
        odd = alpha[c]
        c_alpha[c] = (i-1) //2
        tmp = alpha[c]
        result += c_alpha[c]*tmp
    else:
        t = i //2
        c_alpha[c] = t
        tmp = alpha[c]
        result += tmp*t

if odd !=None:
    result += odd
if not make:
    print("I'm Sorry Hansoo")
else:
    for j in range(25,-1,-1):
        result += alpha[j]*c_alpha[j]
    print(result)