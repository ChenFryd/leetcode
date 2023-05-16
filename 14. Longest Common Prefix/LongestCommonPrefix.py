from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        preFix = strs[0]
        for i in range(1,len(strs)):
            while(not strs[i].startswith(preFix)):
                preFix = preFix[:-1]
            if (preFix == ""):
                return ""
        return preFix

solution = Solution()
print(solution.longestCommonPrefix(["ab","a"]))
#print(solution.longestCommonPrefix(["flower","flow","flight"]))