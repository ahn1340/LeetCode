import math

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = sorted(arr)
        nums = {num: True for num in arr}
        pairs = {num: [] for num in arr}
        
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                num = arr[i] * arr[j]
                if num in nums:
                    pairs[num].append((arr[i], arr[j]))

        counts = {num: None for num in arr}
        for num in arr:
            count = 1
            for pair in pairs[num]:
                i, j = pair
                if i == j:
                    count += counts[i]**2
                else:
                    count += 2 * (counts[i] * counts[j])
            counts[num] = count

        return int(sum(list(counts.values())) % (10**9 + 7))
      
"""
Dynamic Programming. For each num in arr, DP[num] is the number of all possible binary trees with num as root.
Compute it for all nums and sum them.
"""
