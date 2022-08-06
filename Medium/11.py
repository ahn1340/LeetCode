class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ans = 0
        while l != r:
            curr= min(height[l], height[r]) * (r - l)
            ans = max(ans, curr)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
      
"""
two pointer starting from each end. Move the pointer whose height at that index is smaller.
"""
