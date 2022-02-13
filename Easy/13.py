class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        roman2int = {'V': 5, 'L': 50, 'D':500, 'M':1000}
        for i, char in enumerate(s):
            # If C comes before D or M, subtract 100. Else, add 100.
            if char == "C":
                if i != len(s) - 1:
                    if s[i+1] in ['D', 'M']:
                        num -= 100
                    else:
                        num += 100
                else:
                    num += 100
            elif char == 'X':
                if i != len(s) - 1:
                    if s[i+1] in ['L', 'C']:
                        num -= 10
                    else:
                        num += 10
                else:
                    num += 10
            elif char == 'I':
                if i != len(s) - 1:
                    if s[i+1] in ['V', 'X']:
                        num -= 1
                    else:
                        num += 1
                else:
                    num += 1
            else:
                num += roman2int[char]
        return num