import math //math for floor
class Solution:
    def isPalindrome(self, x: int) -> bool:
        numLength = len(str(x))
        for i in range (math.floor(numLength/2)):
            if (str(x)[i] != str(x)[numLength-i-1]):
                return False
        return True

print(Solution().isPalindrome(121))
