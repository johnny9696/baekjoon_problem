import sys
input= sys.stdin.readline

while True:
    text = input()
    if text[0] == '.':
        break
    r_sets = []
    for i in text:
        if i =='(' or i =='[':
            r_sets.append(i)
        elif i ==')':
            if len(r_sets)==0 or r_sets[-1] != '(':
                r_sets.append(i)
                break
            else:
                r_sets.pop()
        elif i ==']':
            if len(r_sets)==0 or r_sets[-1] != '[':
                r_sets.append(i)
                break
            else:
                r_sets.pop()
    if len(r_sets) == 0:
        print('yes')
    else:
        print('no')
