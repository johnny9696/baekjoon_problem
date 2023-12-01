import sys

input = sys.stdin.readline

while True:
    n_list = input()
    #print(n_list)
    if n_list[0] == "#":
        break
    result = 0
    for i in n_list:
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            result+=1
    print(result)