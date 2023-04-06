class Stack():
    def __init__(self):
        self.result = []

    def size(self):
        return len(self.result)

    def empty(self):
        if len(self.result) == 0:
            return 1
        else:
            return 0
    def push(self,val):
        self.result.append(val)

    def pop(self):
        if len(self.result)==0:
            return -1
        else:
            result= self.result[-1]
            del self.result[-1]
            return result

    def top(self):
        if len(self.result) == 0:
            return -1
        else:
            return self.result[-1]




number = int(input())
s_num = Stack()
for i in range(number):
    order = input()
    try:
        order, num = order.split(' ')
    except: order=order


    if order =='pop':
        print(s_num.pop())
    elif order=='push':
        s_num.push(num)
    elif order=='size':
        print(s_num.size())
    elif order=='empty':
        print(s_num.empty())
    elif order=='top':
        print(s_num.top())


