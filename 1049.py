n , m = map(int,input().split())
pack=[]
single=[]
for i in range(0, m):
    p_t,s_t=map(int, input().split())
    pack.append(p_t)
    single.append(s_t)
p_min = min(pack)
s_min = min(single)
sp_min = s_min*6
sp_min = min(sp_min, p_min)
result = sp_min*(n//6)
if p_min<s_min*(n%6):
    result += p_min
else:
    result += s_min*(n%6)
print(result)
