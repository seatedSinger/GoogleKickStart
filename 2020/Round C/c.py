def isPerfectSquare(num):
    left = 1
    right = num
    while left <= right:
        mid = (left + right)//2
        if mid*mid < num:
            left = mid + 1
        elif mid*mid > num:
            right = mid - 1
        else:
            return True
    return False

def f(arr):
    res = 0
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if s == 0 or isPerfectSquare(s):
                res += 1
    return res

a = [2, 2, 6]
print(f(a))

a = [30, 30, 9, 1, 30]
print(f(a))

a = [4, 0, 0, 16]
print(f(a))

a = [4, -10, 12, 16, 20, -42, 32]
print(f(a))


from collections import defaultdict

def f(nums):
    res = 0
    pfs = 0
    largestNum = 0
    ht = defaultdict(int)
    for i in range(len(nums)):
        pfs += nums[i]
        largestNum = max(largestNum, abs(nums[i]))
        j = 0
        while j*j <= (i + 1) * largestNum:
            k = j * j
            if pfs == k:
                res += 1
            remain = pfs - k
            if remain in ht:
                res += ht[remain]
            j += 1
        ht[pfs] += 1
    return res

a = [2, 2, 6]
print(f(a))

a = [30, 30, 9, 1, 30]
print(f(a))

a = [4, 0, 0, 16]
print(f(a))

a = [4, -10, 12, 16, 20, -42, 32]
print(f(a))
