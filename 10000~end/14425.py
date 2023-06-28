import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())

c2n_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

class Tree():
    def __init__(self, data=None):
        self.end = False
        self.next = [None] * 26
        if data:
            self.next[data] = Tree()
    def put(self,data):
        now = data[0]
        if self.next[now] == None:
            self.next[now] = Tree(now)
        if len(data) >1:
            self.next[now].put(data[1:])
            self.end = False
        else:
            self.end = True
    def find(self,data):
        now = data[0]
        if self.next[now] == None:
            return False
        else:
            if len(data)>1:
                return self.next[now].find(data[1:])
            else:
                if self.end:
                    return True
                else:
                    return False

find_letter = Tree()
for _ in range(n):
    letter = list(input())
    letter.remove('\n')
    for i in range(len(letter)):
        letter[i] = c2n_list.index(letter[i])
    find_letter.put(letter)

result = 0
for _ in range(m):
    letter = list(input())
    letter.remove('\n')
    for i in range(len(letter)):
        letter[i] = c2n_list.index(letter[i])
    if find_letter.find(letter):
        result +=1
print(result)