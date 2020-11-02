# Robo 

# All pass

def func(s):
    toDown = 0
    toRight = 0

    curPrefixProduct = 1
    cntStack = []
    num = 0
    for c in s:
        if c.isdigit():
            num = num*10 + int(c)
        elif c == '(':
            cntStack.append(num)
            curPrefixProduct *= num
            num = 0
        elif c == ')':
            cnt = cntStack.pop()
            curPrefixProduct /= cnt
        else:
            if c == 'N':
                toDown -= curPrefixProduct
            elif c == 'S':
                toDown += curPrefixProduct
            elif c == 'W':
                toRight -= curPrefixProduct
            elif c == 'E':
                toRight += curPrefixProduct
    
    
    h = (toDown + 10**9 ) % 10**9
    w = (toRight + 10**9 ) % 10**9
    return w + 1, h + 1

print(func('SSSEEE'))
print(func('N'))
print(func('N3(S)N2(E)N'))
print(func('2(3(NW)2(W2(EE)W))'))

