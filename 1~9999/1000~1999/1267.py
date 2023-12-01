tell = int(input())

n_list = list(map(int,input().split()))

y_result = 0
m_result = 0

for teller in n_list:
    y_result += (10 * (teller//30 + 1))
    m_result += (15 * (teller//60 + 1))


if m_result == y_result:
    print('Y M {}'.format(y_result))
elif m_result < y_result:
    print('M {}'.format(m_result))
elif y_result < m_result:
    print('Y {}'.format(y_result))