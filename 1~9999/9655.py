n = int(input())
c = 0
c = n // 3  + n % 3
if c % 2 == 0:
    print('CY')
else:
    print('SK')