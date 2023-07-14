m,n = map(int,input().split())
site_dict = dict()
for _ in range(m):
    site, passward= map(str, input().split())
    site_dict[site] = passward

for _ in range(n):
    print(site_dict[input()])