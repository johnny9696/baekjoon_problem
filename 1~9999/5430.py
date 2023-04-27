T= int(input())
for test_case in range(T):
    act = input()
    length = int(input())
    num_list = input()
    num_list = num_list[1:-1]
    re = False
    er = False
    if num_list:
        num_list = list(map(int,num_list.split(',')))
        sp = 0
        for j in act:
            if j == 'R':
                if re:
                    re = False
                else:
                    re = True
                if sp ==0:
                    sp = len(num_list)-1
                else:
                    sp = 0
            else:
                try:
                    num_list.pop(sp)
                    if sp !=0:
                        sp += -1
                except:
                    er = True
                    break

        if num_list:
            if re:
                num_list.reverse()
                print(num_list)
            else:
                print(num_list)
        else:
            if er:
                print('error')
            else:
                print(num_list)
    else:
        if 'D' in act:
            print('error')
        else:
            print('[]')

