class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        # make a stack
        order = []
        for char in s:
            if s[0] in parentheses:
                return False
            if not order:
                order.append(char)
                continue
            if char in parentheses:
                if order[-1] == parentheses[char]:
                    order.pop()
                else:
                    return False
            else:
                order.append(char)
        return not order
        