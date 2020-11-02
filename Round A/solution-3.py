import heapq

"""
    1st: heap
    11pts   Pass
    18psts  Pass
"""
def f(arr, k):
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

        higherDiff = right - mid
        
        heapq.heappush(pq, (-diff, left, mid))
        heapq.heappush(pq, (-higherDiff, mid, right))
        k -= 1
    return -pq[0][0]
"""
4
3 1
100 200 230
3
5 2
10 13 15 16 17
5 6
9 10 20 26 30
8 3
1 2 3 4 5 6 7 10
"""

a = [100, 200 ,230]
b = 1
print(f(a, b))

a = [10, 13, 15, 16, 17]
b = 2
print(f(a, b))
