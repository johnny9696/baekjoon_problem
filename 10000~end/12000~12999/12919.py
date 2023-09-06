s = list(input())
s = s[:]
t = list(input())
t = t[:]

len_s = len(s)
len_t = len(t)
task = len_t - len_s

def BFS(text, depth):
    result = False
    if depth == task:
        if text == s:
            return True
        else:
            return False
    else:
        if text[-1] == 'A':
            result = BFS(text[:-1], depth + 1)
            if result:
                return result
        if text[0] == 'B':
            tmp = text[1:]
            tmp.reverse()
            result = BFS(tmp, depth + 1)
            if result:
                return result
    return result
if BFS(t, 0):
    print(1)
else:
    print(0)