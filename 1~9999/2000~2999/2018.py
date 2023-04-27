m =  int(input())

c = m//4
result = 0
for i in range(1,c+2):
    odd = 2*i - 1
    even = 2*i
    if m//odd*2 >= odd:
        if m%odd ==0 :
            result +=1
    if m//even*2 >= even:
        if m%even == i:
            result +=1
print(result)
