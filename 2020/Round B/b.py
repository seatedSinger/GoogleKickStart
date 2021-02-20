'''
Passed
'''


def func(nums, D):
    rightMost = D
    for i in range(len(nums)-1, -1, -1):
        rightMost = nums[i] * (rightMost // nums[i])
    return rightMost


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N, D = [int(s) for s in input().split(" ")]
    arr = [int(s) for s in input().split(" ")]
    res = func(arr, D)
    print("Case #{}: {}".format(i, res))
