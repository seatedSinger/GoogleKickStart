"""
    approach: sort
    Time    O(NlogN)
    Space   O(1)
    5pts    Pass
    7pts    Pass
"""
def func(arr, k):
    arr = sorted(arr)
    total = 0
    for i in range(len(arr)):
        total += arr[i]
        if total > k:
            return i
    return len(arr)

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input()().split(" ")]
    arr = [int(s) for s in input()().split(" ")]
    res = func(arr, k)

    print("Case #{}: {}".format(i, res))

# a = [20, 90, 40, 90]
# b = 100
# print(f(a, b))
