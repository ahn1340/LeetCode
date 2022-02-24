class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cumsum = 0
        cumsum_list = [0]
        for num in nums:
            cumsum += num
            cumsum_list.append(cumsum)
        
        d = {}
        for cumsum in cumsum_list:
            key = cumsum - k
            if key in d:
                ans += d[key]
            if cumsum in d:
                d[cumsum] += 1
            else:
                d[cumsum] = 1
        
        return ans
"""
Idea:
create cumulative sum array, such where value of ith index = num[0] + num[1] + ... + num[i].
This way, sum of subarray [i:j] can be easily computed as cumsum_list[j] - cumsum_list[i-1].
Then initialize a dict where key: cumsum, value: num occurence
Then, iterate over the cumsum list. At each step, check if current cumsum - k is in dict.
If yes, add its value to final answer.
Finally, if current cumsum is in dict, increment its value. If not, add cumsum to dict with value 1.
"""
