search_list = [1,3,5,7,9]
def check(num):
    for i in range(2,num//2+2):
        if num%i == 0:
            return False
    return True

def search_Tree(c_num, c_depth, m_depth):
    if c_depth == m_depth:
        print(c_num)
        return 0
    c_num = c_num * 10
    for i in search_list:
        c_num +=  i
        if check(c_num):
            search_Tree(c_num,c_depth+1, m_depth)
        c_num += -i

n = int(input())
s_list = [2,3,5,7]
for i in s_list:
    search_Tree(i,1,n)