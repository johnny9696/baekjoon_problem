p_list = [1,1,1,2,2]

for i in range(5,101):
    p_list.append(p_list[i-1]+p_list[i-5])

T = int(input())

for _ in range(T):
    print(p_list[int(input())-1])
