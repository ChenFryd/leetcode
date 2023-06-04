class Solution:
    def canConstruct(self, ransoNote: str, magazine: str) -> bool:
        required = {}
        for char in ransoNote:
            required[char] = required.get(char,0)+1
        for charMagazine in magazine:
            if charMagazine in required and required[charMagazine] > 0:
                required[charMagazine] -= 1
        for value in required.values():
            if value > 0:
                return False
        return True


sol = Solution()
print(sol.canConstruct("aa","aab"))
print(sol.canConstruct("aa","ab"))
print(sol.canConstruct("aa","aabb"))
print(sol.canConstruct("aab","baa"))
print(sol.canConstruct("bg","efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))

