"""
    initial : brute force | O(N^M) | O(NM)
    9pts    Pass
    15pts   Fail
"""
class Solution(object):
    
    def __init__(self):
        self.res = 0

    def sol(self, stacks, k):   
        self.dfs(stacks, k, 0)
        return self.res
        
    def dfs(self, stacks, k, total):
        if len(stacks) == 0:
            if k == 0:
                self.res = max(self.res, total)
            return
        stack = stacks[0]
        newStacks = stacks[1:]
        self.dfs(newStacks, k, total)
        acc = 0
        for i in range(len(stack)):
            acc += stack[i]
            if k - (i+1) >= 0:
                self.dfs(newStacks, k - (i+1), total + acc)

s = Solution()
a = [
    [10, 10, 100, 30],
    [80, 50, 10, 50],
]
b = 5
print(s.sol(a, b))
