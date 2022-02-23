class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # case where k = 0: find all nums that occur more than once
        if k == 0:
            ans = 0
            d = {}
            for num in nums:
                if num in d:
                    d[num] += 1
                else:
                    d[num] = 1
            for k, v in d.items():
                if v > 1:
                    ans += 1
            return ans

        # case where k > 1
        nums = list(set(nums))

        d = self.create_dict(nums, k)
        ans = 0
        for num in nums:
            if num in d:
                if d[num] is not None:
                    ans += len(d[num])
                    for n in d[num]:
                        d[n] = None
                    d[num] = None

        return ans

    def create_dict(self, nums, k):
        """
        Inputs
        nums: list of numbers (only unique)
        k: difference
        Outputs
        d: dictionary where key is a number whose difference with its
        values is k. Values exist in nums, but key may not exist in nums.
        """
        d = {}
        for num in nums:
            pair1, pair2 = num + k, num - k
            if pair1 in d:
                d[pair1].append(num)
            else:
                d[pair1] = [num]
            if pair2 in d:
                d[pair2].append(num)
            else:
                d[pair2] = [num]

        return d