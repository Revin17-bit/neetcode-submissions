class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {'(':')','{':'}','[':']'}
        stack = []
        for i in s:
            if i in bracket:
                stack.append(i)
            if i not in bracket:
                if not stack:
                    return False
                if bracket[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        return stack == []
            

                

