import sys
input = sys.stdin.readline
length = int(input())
text= list(input().split())
switch = [int(i) for i in text]

switch.insert(0,0)
case = int(input())
for _ in range(case):
    sex, num = map(int,input().split())
    if sex == 1:
        k = 1
        while num*k<=length:
            switch[num*k] = (switch[num*k]+1)%2
            k+=1
    else:
        dist = min(num,length - num+1)
        switch[num] = (switch[num] + 1) % 2
        for i in range(1,dist):
            if switch[num+i] ==  switch[num-i]:
                switch[num+i] = (switch[num+i]+1)%2
                switch[num-i] = (switch[num-i]+1)%2
for  i in range(1, length+1):
    print(switch[i],end=' ')
