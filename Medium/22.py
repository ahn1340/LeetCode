class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        string = ''
        opening_num = n
        closing_num = n
        return self.recursive_generate(opening_num, closing_num, string, n * 2)

    def recursive_generate(self, opening_num, closing_num, string, n, result=None):
        if result is None:
            result = []
        # base case
        if n == 1:
            result.append(string + ')')
        else:
            # case 1. add new opening parenthesis
            if opening_num > 0:
                string1 = string + '('
                self.recursive_generate(opening_num - 1, closing_num, string1, n - 1, result)
            # case 2. add new closing parenthesis if possible
            if opening_num < closing_num:
                string2 = string + ')'
                self.recursive_generate(opening_num, closing_num - 1, string2, n - 1, result)

        return result

