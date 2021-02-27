# O(N) | O(N)

def func(A):
    if len(A) <= 1:
        return 0
    gCount = 0
    curDiff = 0
    curCount = 0
    for i in range(1, len(A)):
        diff = A[i] - A[i-1]
        if diff == curDiff:
            curCount += 1
        else:
            curDiff = diff
            curCount = 1
        gCount = max(gCount, curCount)
    return gCount + 1


print(func([5, 5, 4, 5, 5, 5, 4, 5, 6]))
print(func([5, 4, 3, 2, 1, 2, 3, 4, 5, 6]))
print(func([5,5,5]))
