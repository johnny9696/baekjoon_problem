f_lenght, p_length = map(int, input().split())
text = list(input())
pass_list= list(map(int, input().split()))
result = 0

for i in range(f_lenght-p_length+1):
    if i == 0 :
        temp = text[:p_length]
        check_list = [temp.count('A'),temp.count('C'), temp.count('G'), temp.count('T')]
    else:
        if text[i-1]=='A':
            check_list[0] += -1
        elif text[i-1] =='C':
            check_list[1] += -1
        elif text[i-1] =='G':
            check_list[2] += -1
        else:
            check_list[3] += -1
        if text[i+p_length-1]=='A':
            check_list[0] += 1
        elif text[i+p_length-1] =='C':
            check_list[1] += 1
        elif text[i+p_length-1] =='G':
            check_list[2] += 1
        else:
            check_list[3] += 1
    if check_list[0] >=pass_list[0] and  check_list[1] >=pass_list[1] and  check_list[2] >=pass_list[2] and check_list[3] >=pass_list[3]:
        result += 1
print(result)
