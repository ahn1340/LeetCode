from string import ascii_lowercase

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",\
                "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",\
                "...-",".--","-..-","-.--","--.."]
        table = {c: code for c, code in zip(ascii_lowercase, code)}
        d = {}
        count = 0
        for word in words:
            code = ''
            for c in word:
                code += table[c]
            if code not in d:
                d[code] = True
                count += 1

        return count
            
"""
convert strings into code, check if it is already seen. If not, increment counter. Finally, return counter. Time: O(nk), Space: O(nk)
where n: number of words, k: maximum length of word.
"""
