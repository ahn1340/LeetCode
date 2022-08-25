class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        subarr_lens = [0]
        consec = False
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                consec = True
                subarr_lens[-1] += 1
            else:
                if consec == True:
                    subarr_lens.append(0)
                    consec = False
        
        ans = 0
        for num in subarr_lens:
            ans += (num * (num + 1)) // 2
        
        return ans

      
"""
Get all maximal arithmetic slices. Then, compute the number of subarrays of len > 3 for each maximal arithmetic slice,
and return the sum.
Time: O(n), space: O(n), where len(num).
"""
