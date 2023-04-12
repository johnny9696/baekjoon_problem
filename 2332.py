def t2n(text):
    result = str()
    for i in text:
        if i == 'i' or i=='j':
            result = result + '1'
        elif i == 'a' or i =='b' or i == 'c':
            result = result + '2'
        elif i == 'd' or i =='e' or i == 'f':
            result = result + '3'
        elif i == 'g' or i =='h' :
            result = result + '4'
        elif i == 'k' or i =='l' :
            result = result + '5'
        elif i == 'm' or i =='n':
            result = result + '6'
        elif i == 'p' or i =='r' or i == 's':
            result = result + '7'
        elif i == 't' or i =='u' or i == 'v':
            result = result + '8'
        elif i == 'w' or i =='x' or i == 'y':
            result = result + '9'
        else:
            result = result + '0'
    return result

def find_list(num, num_list):
    result = []
    if len(num) == 0:
        return result
    for i , t_num in enumerate(num_list):
        #print(num[:len(t_num)], t_num)
        if num[:len(t_num)] == t_num:
            t_result = find_list(num[len(t_num):],num_list)
            if t_result != -1:
                result.append(i)
                result = result + t_result
                return result
    return -1


num = input()
n = int(input())
text_list = []
num_list = []
for i in range(0,n):
    text = input()
    text_list.append(text)
    num_list.append(t2n(text))

result = find_list(num, num_list)

if result == -1 :
    print(0)
    print('No solution.')
else:
    print(len(result))
    for i in result:
        print(text_list[i])

