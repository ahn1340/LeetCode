class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        zeros = [-1]
        negs = []
        first_neg = None
        last_neg = None
        num_neg = 0

        for i, num in enumerate(nums):
            if num == 0:
                negs.append((first_neg, last_neg, num_neg % 2))
                zeros.append(i)
                first_neg = None
                num_neg = 0
            elif num < 0:
                num_neg += 1
                if first_neg is None:
                    first_neg = i
                last_neg = i
        negs.append((first_neg, last_neg, num_neg % 2))
        zeros.append(len(nums))

        best = 0
        for i, (first, last, odd) in enumerate(negs):
            start, end = zeros[i], zeros[i+1]
            if odd:
                best = max(best, max(last - start - 1, end - first - 1))
            else:
                best = max(best, end - start - 1)
        
        return best
    
"""
Segment array by zeros. Then, if there are even number of negative numbers,
then the length of the segment is the candidate subarray length
If there are odd number of negative numbers, then the maximum legnth positive
product sub array is either from start of that segment to the last negative number
or from the first negative number to the end of the segment.
Finally, return the longest subarray candidate's length.
"""
