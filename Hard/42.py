class Solution:
    def trap(self, height: List[int]) -> int:
        highest = -1
        highest_idx = 0
        for i, h in enumerate(height):
            if highest < h:
                highest = h
                highest_idx = i

        ans = 0
        ans += self.traverse_until_highest(height, highest_idx, 'left')
        ans += self.traverse_until_highest(height, highest_idx, 'right')

        return ans
    
    def traverse_until_highest(self, height, highest_idx, direction):
        total, cur_max, area_sum = 0, 0, 0
        if direction == 'left':
            sequence = range(highest_idx+1)
        elif direction == 'right':
            sequence = range(len(height)-1, highest_idx-1, -1)
        
        for i in sequence:
            h = height[i]
            if cur_max <= h:
                cur_max = h
                total += area_sum
                area_sum = 0
            else:
                area_sum += cur_max - h

        return total

"""
Idea:
First get the index of the highest wall. Then, traverse twice, once from the start of the array and once from the end,
both until the highest wall. At each step, check if current wall is at least as high as the highest wall we've seen so far.
If no, we accumulate the difference between current highest wall and current wall. If yes, we update total area with the 
accumulated area sum, set current highest wall value as current wall height and reset area sum.
Repeat until we reach the highest wall.
Time Complexity: O(n)
Space Complexity: O(1)
"""
