def f(N, A, B, C):

    a = A - C
    b = B - C

    if C > A or C > B or a + b + C > N:
        return 'IMPOSSIBLE'

    if a + b + C == 1 and N >= 2:
        return 'IMPOSSIBLE'

    if N == 1:
        return '1'
    elif N == 2:
        if C == 2:
            return '1 1'
        elif A == 2:
            return '1 2'
        elif B == 2:
            return '2 1'
    else:
        res = []
        for i in range(a):
            res.append(2)
        for i in range(C):
            res.append(3)
        for i in range(b):
            res.append(2)
        remain = N - (A + B - C)
        if remain > 0:
            res = res[:1] + (remain * [1]) + res[1:]
        return ' '.join([str(x) for x in res])


print(f(4, 1, 3, 1))
print(f(4, 4, 4, 3))
print(f(5, 3, 3, 2))
print("-----")
print(f(14, 5, 7, 3))
print(f(1, 1, 1, 1))
print(f(5, 1, 1, 1))
print(f(5, 2, 2, 2))
print(f(5, 3, 3, 3))

print(f(5, 4, 2, 2))
print(f(5, 2, 4, 2))
print(f(5, 4, 2, 1))
print(f(5, 2, 4, 1))
