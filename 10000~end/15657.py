import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int,input().split())
n_list = list(map(int,input().split()))
n_list.sort()

c = n**m
count = 0

def DFS(mat,result, depth):
    global count
    global c
    if depth == m :
        for i in mat:
            count +=1
            if count != c:
                print(result + str(i)+'\n')
            else:
                print(result + str(i))
    else:
        for i in range(len(mat)):
            DFS(mat[i:],result + str(mat[i])+' ', depth + 1)

DFS(n_list,'', 1)
