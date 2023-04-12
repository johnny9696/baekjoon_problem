from sys import stdin
counter=int(stdin.readline())
stack=[]
for i in range(counter):
    data=int(stdin.readline())
    if data==0:
        del stack[len(stack)-1]
    else:
        stack.append(data)
print(sum(stack))