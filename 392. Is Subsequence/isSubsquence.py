class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        indexSubstring, indexSuperSetString = 0,0
        while indexSubstring<len(s) and indexSuperSetString < len(t):
            if s[indexSubstring] == t[indexSuperSetString]:
                indexSubstring += 1
            indexSuperSetString += 1
        return True if indexSubstring == len(s) else False