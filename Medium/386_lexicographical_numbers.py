import sys
sys.setrecursionlimit(10**6)

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        length = len(str(n))
        l = []
        start = 0
        def backtrack(curr):
            if 1 <= curr <= n:
                l.append(curr)
            for i in range(0, 10):
                nxt = curr * 10 + i
                if 1 <= nxt <= n:
                    backtrack(nxt)
            return
        backtrack(start)

        return l

"""
Backtracking (DFS) with Time: O(n), Space: O(1).
"""
