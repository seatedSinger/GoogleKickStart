import imp


import heapq

def func(arr, k):
    pq = []
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        heapq.heappush(pq, (
            -diff,
            min(arr[i], arr[i-1]),
            max(arr[i], arr[i-1])
        ))
    while k > 0:
        negativDiff, left, right = heapq.heappop(pq)

        diff = (-negativDiff) // 2
        mid = left + diff

        # consider: left = 10, right = 13
        # we want to split it into: (1, 10, 11), (2, 11, 13)
        higherDiff = right - mid

        heapq.heappush(pq, (-diff, left, mid))
        heapq.heappush(pq, (-higherDiff, mid, right))
        k -= 1
    return -pq[0][0]


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input()().split(" ")]
    arr = [int(s) for s in input()().split(" ")]
    res = func(arr, k)
    print("Case #{}: {}".format(i, res))
