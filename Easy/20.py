class Solution:
    def isValid(self, s: str) -> bool:
        """
        use queue to determine if input is valid
        """
        stack = []  # LIFO stack
        # if opening bracket, add to stack. If closing, pop from stack and check validity
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            else:
                # if no items in stack, s is not valid.
                if len(stack) == 0:
                    return False
                else:
                    elem = stack.pop()
                    if elem != char:
                        return False
        # if there are items remaining in stack, s is not valid.
        if len(stack) == 0:
            return True
        else:
            return False