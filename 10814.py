from sys import stdin
counter=int(stdin.readline())
data=[]
for i in range(counter):
    in_data=stdin.readline().split()
    data.append(in_data)
    #print(data[i])
data.sort(key=lambda a:int(a[0]))
for i in range(counter):
    #print(data[i])
    print(data[i][0],data[i][1])