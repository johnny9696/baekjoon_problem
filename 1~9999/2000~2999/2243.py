class linked_list():
    def __init__(self, b=None,c=None, next=None):
        self.num = b
        self.count = c
        self.next = next
    def candy_in(self,b,c):
        if self.num ==None:
            self.num = b
            self.count = c
        else:
            if b > self.num:
                if self.next == None :
                    self.next=linked_list(b,c)
                else:
                    if b > self.next.num:
                        self.next.candy_in((b,c))
                    else:
                        temp = linked_list(b,c, self.next)
                        self.next = temp
            else:
                temp = linked_list(self.num,self.count, self.next)
                self.num = b
                self.count = c
                self.next = temp
    def candy_out(self,b,c):
        if self.num !=b:
            temp = self.next.candy_out(b,c)
            if temp != None:
                self.next = temp
        else:
            self.count = self.count + c
            if self.count == 0:
                return self.next
            else:
                return None
    def a_candy_out(self,b,c_num):
        if self.count + c_num <b:
            temp = self.next.a_candy_out(b, c_num+self.count)
            if temp != None:
                self.next= temp
        else:
            self.count = self.count -1
            print(self.num)
            if self.count == 0:
                return self.next
            else:
                return None

n = int(input())
l_list= linked_list()
for i in range(n):
    in_list = input().split()
    a = int(in_list[0])
    b = int(in_list[1])
    if len(in_list) >2:
        c = int(in_list[2])
    if a == 1:
        l_list.a_candy_out(b,0)
    else:
        if c<0:
            l_list.candy_out(b,c)
        else:
            l_list.candy_in(b,c)

