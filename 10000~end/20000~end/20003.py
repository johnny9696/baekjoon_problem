import sys
input = sys.stdin.readline

test_case = int(input())

child_list = []
parents_list = []

for _ in range(test_case):
    c,p = map(int,input().split())
    i = 2
    while i <= min(c,p):
        if c % i == 0 and p % i ==0:
            c=c//i
            p=p//i
        else:
            i+=i
    child_list.append(c)
    parents_list.append(p)

mp = max(parents_list)
while True:
    div = True
    for i in parents_list:
        if mp%i != 0:
            div = False
    if div:
        break
    mp += 1

for i, data in enumerate(parents_list):
    tmp = mp//data
    child_list[i] = child_list[i] * tmp
c_min = min(child_list)
i=1
div_num = 1
while i <= c_min:
    div = True
    for j in child_list:
        if j%i != 0 :
            div = False
    if div:
        div_num = i
    i+=1

cp_num = min(div_num,mp)
i = 2
while i<cp_num:
    if div_num %i ==0 and mp % i == 0:
        div_num = div_num // i
        mp = mp // i
    else:
        i+=1


print(div_num,end=' ')
print(mp)

