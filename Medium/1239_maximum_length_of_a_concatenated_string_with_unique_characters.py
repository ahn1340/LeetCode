class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # eliminate strings with duplicate
        new_arr = []
        for string in arr:
            if len(set(string)) == len(string):
                new_arr.append(string)

        l = ['']
        for i, s1 in enumerate(new_arr):
            for s2 in l:
                s2_tmp = set(s2)
                if all([c not in s2_tmp for c in s1]):
                    l.append(s2 + s1)
        return len(max(l, key=lambda x: len(x)))
        

"""
Check all possible solutions. Possible since len(arr) <= 16.
Time: O(2^n * k), Space: O(nk), where n: len(arr), k: maximum string length in arr.
"""
