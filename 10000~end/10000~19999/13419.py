import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    text = list(input())
    text =text[:-1]
    result_a = ''
    result_b= ''
    for i in range(len(text)):
        if i % 2 == 0:
            result_a +=text[i]
        else:
            result_b +=text[i]
    if len(text)%2 == 1:
        print(result_a+result_b)
        print(result_b+result_a)
    else:
        print(result_a)
        print(result_b)