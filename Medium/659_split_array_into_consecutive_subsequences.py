class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # parse array
        arrs = []
        counter = 0
        curr = nums[0]
        for num in nums:
            if num == curr:
                counter += 1
            else:
                arrs.append((curr, counter))
                curr = num
                counter = 1
        arrs.append((curr, counter))
        
        # split array
        arrss = []
        curr = nums[0] - 1
        tmp = []
        for pair in arrs:
            if curr + 1 == pair[0]:
                tmp.append(pair)
                curr += 1
            else:
                arrss.append(tmp)
                tmp = [pair]
                curr = pair[0]
        arrss.append(tmp)
        
        for arr in arrss:
            if len(arr) < 3:
                return False
            more, prev, curr = 0, 0, 0
            prev_val = arr[0][0] - 1
            for val, freq in arr:
                new_prev = curr
                # if freq - new_prev < 0: not enough.
                if freq - (curr + prev) < 0:
                    return False
                new_more = min([freq - curr, more + prev])
                new_curr = freq - (new_more + new_prev)
                more, prev, curr = new_more, new_prev, new_curr
                prev_val = val

            # final check
            if (prev != 0 or curr != 0):
                return False
        return True
      
"""
TODO: make the code cleaner, and explain the idea
Time: O(n), Space: O(n), where n: len(nums).
"""
