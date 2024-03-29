def f(A):
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

# print(f([10, 7, 4, 6, 8, 10, 11]))
# print(f([9, 7, 5, 3]))
# print(f([5, 5, 4, 5, 5, 5, 4, 5, 6]))
# print(f([5, 4, 3, 2, 1, 2, 3, 4, 5, 6]))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    k = int(input())
    arr = [int(s) for s in input().split(" ")]
    res = f(arr)

    print("Case #{}: {}".format(i, res))
    
