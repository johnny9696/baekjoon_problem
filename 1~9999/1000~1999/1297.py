"""
대각선  D 높이 H 너비  W
sqrt(D^2 /(H^2 + W^2) )= X
X*H X*W
"""
import math
D,H,W = map(float,input().split())
x = math.sqrt(D**2/(H**2+W**2))
print(int(x*H), int(x*W))