R,G,B = map(int,input().split())

"""
3개 로 나눈 몫
"""
result = R//3 + G//3 + B//3
R = R%3
G = G%3
B = B%3

while R>0 or G>0 or B>0:
    if R>0 and G>0 and B>0 :
        result+=1
        R-=1
        G-=1
        B-=1
    else:
        if R>0 and G>0:
            result+=1
            R-=1
            G-=1
        elif R>0 and B>0:
            result+=1
            R-=1
            B-=1
        elif G>0 and B>0:
            result+=1
            G-=1
            B-=1
        else:
            if R == 2:
                result+=1
                R += -2
            elif R==1:
                result+=1
                R -=1
            if G == 2:
                result+=1
                G +=-2
            elif G == 1:
                result += 1
                G -= 1
            if B == 2:
                result+=1
                B += -2
            elif B == 1:
                result += 1
                B -= 1
print(result)