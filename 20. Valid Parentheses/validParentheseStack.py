class Solution:
    def isValid(self, s: str) -> bool:
        map = {")":"()","]":"[","}":"{"}
        stack = []
        
        for c in s:
            if c not in s:
                stack.append(c)
                continue
            if not stack or stack[-1] != c:
                return False
            stack.pop()
            
        return not stack