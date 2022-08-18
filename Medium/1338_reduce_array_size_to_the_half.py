class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        sorted_d = sorted([(k, v) for k, v in d.items()], key=lambda x: x[1], reverse=True)

        half = len(arr) // 2
        counter = 0
        for (k, v) in sorted_d:
            half -= v
            counter += 1
            if half <= 0:
                break
                
        return counter

"""
Store integers and their fequency in a hash map. Then, sort them (in decreasing order) according to
the the frequencies. Then, Count how many of them we can remove from the beginning to reduce
the size to the half. Time: O(nlogn), space: O(n) where n: length of array.
"""
