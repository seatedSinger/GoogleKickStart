
def func(s):
    cntStack = []
    strStack = [""]
    num = 0
    for c in s:
        if c.isdigit():
            num = num*10 + int(c)
        elif c == '(':
            cntStack.append(num)
            num = 0
            strStack.append("")
        elif c == ')':
            cnt = cntStack.pop()
            cur = strStack.pop()
            temp = cnt * cur
            strStack[-1] += temp
        else:
            strStack[-1] += c
    return strStack.pop()


print(func('SSSEEE'))
print(func('N'))
print(func('N3(S)N2(E)N'))
print(func('2(3(NW)2(W2(EE)W))'))


def func(s):
    intructions = func(s)
    toDown = 0
    toRight = 0
    for c in intructions:
        if c == 'N':
            toDown -= 1
        elif c == 'S':
            toDown += 1
        elif c == 'W':
            toRight -= 1
        elif c == 'E':
            toRight += 1
    h = (toDown + 10**9) % 10**9
    w = (toRight + 10**9) % 10**9
    return w + 1, h + 1


print(func('SSSEEE'))
print(func('N'))
print(func('N3(S)N2(E)N'))
print(func('2(3(NW)2(W2(EE)W))'))

# # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# # This is all you need for most Code Jam problems.
# t = int(raw_input())  # read a line with a single integer
# for i in range(1, t + 1):
#     arr = raw_input()
#     res = f(arr)
#     print("Case #{}: {} {}".format(i, res[0], res[1]))


print("-----")


def f(s):
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

    h = (toDown + 10**9) % 10**9
    w = (toRight + 10**9) % 10**9
    return w + 1, h + 1


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    arr = input()
    res = f(arr)
    print("Case #{}: {} {}".format(i, res[0], res[1]))
