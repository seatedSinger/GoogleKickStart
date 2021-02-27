# All Pass

def func(arr, K):
    res = 0
    target = K
    for i in range(len(arr)):
        if arr[i] != target:
            target = K
        if arr[i] == target:
            target -= 1
            if target == 0:
                res += 1
                target = K
    return res

a = [1,2,3,7,9,3,2,1,8,3,2,1]
b = 3
print(func(a, b))

a = [101, 100, 99,98]
b = 2
print(func(a, b))

a = [100, 7, 6, 5, 4, 3, 2, 1, 100]
b = 6
print(func(a, b))
