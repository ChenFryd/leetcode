class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesDict = {")":"(","]":"[","}":"{"}
        i=1
        while i<len(s):
            if s[i-1]==parenthesesDict.get(s[i],"$") and i>0:
                s=s[:i-1] + s[i+1:]
                i -= 2
            i += 1
        return s==""
        
solution = Solution()
print(solution.isValid("([])"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(){}}{"))
