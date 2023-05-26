class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        
        setChars = set()
        left = 0
        maxLength =0
        for right in range(len(s)):
        
            while not setChars.isdisjoint(s[right]):
                setChars.remove(s[left])
                left+=1
            setChars.add(s[right])
            maxLength = max(maxLength,right-left+1)
        return maxLength

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb")) #3
print(sol.lengthOfLongestSubstring("bbbbb")) #1
print(sol.lengthOfLongestSubstring("pwwkew")) #3
print(sol.lengthOfLongestSubstring("")) #0