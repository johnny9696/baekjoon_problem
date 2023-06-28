def panhi(x):
    num_list1 = []
    num_list2 =[]
    while x>0:
        tmp = x%10
        x= x//10
        num_list1.append(tmp)
        num_list2.insert(0,tmp)
    if num_list2==num_list1:
        return True
    else:
        return False

n = int(input())
sosu = [False for _ in range(1003002 + 1)]
sosu[0] = True
sosu[1] = True
for i in range(2, len(sosu)//2+1):
    if sosu[i] == 0:
        c = 2
        while i*c<len(sosu):
            sosu[i*c] = True
            c+=1

while True:
    if panhi(n) and sosu[n] == False:
        print(n)
        break
    n += 1
