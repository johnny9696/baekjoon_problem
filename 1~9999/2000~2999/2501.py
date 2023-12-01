n, k =map(int,input().split())

sub_list = [0]

for i in range(1, n+1):
    if n % i == 0:
        sub_list.append(i)

if len(sub_list) > k:
    print(sub_list[k])
else:
    print(0)