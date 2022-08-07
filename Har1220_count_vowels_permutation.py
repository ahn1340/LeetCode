class Solution:
    def countVowelPermutation(self, n: int) -> int:
        v = [1, 1, 1, 1, 1]
        for i in range(n-1):
            v = [v[1]+v[2]+v[4], v[0]+v[2], v[1]+v[3], v[2], v[2]+v[3]]
        return sum(v) % (10**9 + 7)

"""
Basic dynamic programming
"""
