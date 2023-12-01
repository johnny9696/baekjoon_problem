import sys

input = sys.stdin.readline

n = int(input())
people = {}
for _ in range(n):
    name, how = map(str, input().split())
    if how == 'enter':
        people[name] = how
    else:
        if people[name]:
            del people[name]

for p in sorted(people,reverse=True):
    print(p)