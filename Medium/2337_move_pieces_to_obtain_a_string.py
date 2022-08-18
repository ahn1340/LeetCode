class Solution:
    def canChange(self, start: str, target: str) -> bool:
        src = []
        tgt = []
        for i, (s, t) in enumerate(zip(start, target)):
            if s != '_':
                src.append((i, s))
            if t != '_':
                tgt.append((i, t))
        if len(src) != len(tgt):
            return False
        for s, t in zip(src, tgt):
            if s[1] != t[1]:
                return False
            elif s[1] == 'L':
                if s[0] < t[0]:
                    return False
            elif s[1] == 'R':
                if s[0] >t[0]:
                    return False
        return True

"""
Store index of each L and R of start and target. Then, create one-to-one mappings for each src[i]
and tgt[i]. For all is, if src[i] and tgt[i] are different, return False. If not, check if we can
move src[i] to locate it where tgt[i] is. If yes for all src[i], return True.
Time: O(n), Space: O(n) where n: length of start.
"""
