import sys

input = sys.stdin.readline

n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse = True)
max_weight = 0
sum_weight = 0

for i, weight in enumerate(rope):
    max_weight = max(max_weight, weight * (i+1))

print(max_weight)