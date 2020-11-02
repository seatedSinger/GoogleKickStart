# All Pass

def func(nums, D):
    right = D
    for i in range(len(nums)-1, -1, -1):
        right = nums[i] * (right // nums[i])
    return right

a = [3, 7, 2]
print(func(a, 10))