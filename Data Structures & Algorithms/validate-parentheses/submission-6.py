class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        # make a stack
        order = []
        if len(s) == 1:
            return False
        for char in s:
            if not order:
                order.append(char)
                continue
            if char in parentheses.keys():
                if order[-1] == parentheses[char]:
                    order.pop()
                else:
                    return False
            else:
                order.append(char)
        return not order
        