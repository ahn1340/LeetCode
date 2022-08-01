import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:    
        idxs = []
        curr = k - 1
        for i in range(n - 1, 0, -1):
            interval = math.factorial(i)
            div, rem = divmod(curr, interval)
            idxs.append(div)
            curr = rem
        nums = [str(i) for i in range(1, n+1)]
        ans = ""
        for idx in idxs:
            ans = ans + nums.pop(idx)
            
        return ans + nums.pop(0)
