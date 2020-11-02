  
"""
    approach: sort
    Time    O(NlogN)
    Space   O(1)
    5pts, 7pts Pass pass
"""
def f(arr, k):
    arr = sorted(arr)
    total = 0
    for i in range(len(arr)):
        total += arr[i]
        if total > k:
            return i
    return len(arr)


t = int(input())
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    arr = [int(s) for s in input().split(" ")]
    res = f(arr, k)

    print("Case #{}: {}".format(i, res))

a = [20, 90, 40, 90]
b = 100
print(f(a, b))

# a = [30, 30, 10, 10]
# b = 50
# print(f(a, b))

# a = [999, 999, 999]
# b = 300
# print(f(a, b))