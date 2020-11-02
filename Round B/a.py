# All Pass

def func(nums):
    res = 0
    for i in range(1, len(nums)-1):
        if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
            res += 1
    return res
