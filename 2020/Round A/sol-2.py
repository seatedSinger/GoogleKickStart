class Solution(object):
    
    def __init__(self):
        self.res = 0

    def func(self, stacks, k):   
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

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input())
for i in range(1, t + 1):
    n, _, k = [int(s) for s in input()().split(" ")]
    stacks = []
    for _ in range(n):
        stack = [int(s) for s in input()().split(" ")]
        stacks.append(stack)
    s = Solution()
    res = s.f(stacks, k)
    print("Case #{}: {}".format(i, res))
