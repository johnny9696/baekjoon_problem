import sys

n_list = list(map(int,input().split()))

#a,b a,c ,a,d
#c,d b,d  b,c
gap_time = [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
min_gap = sys.maxsize
for ta,tb in gap_time:
    tmp1 = n_list[ta[0]] + n_list[ta[1]]
    tmp2 = n_list[tb[0]] + n_list[tb[1]]
    gap = abs(tmp1-tmp2)
    min_gap = min(min_gap,gap)
print(min_gap)