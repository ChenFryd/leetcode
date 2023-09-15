from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numDict = {}
        for num in nums:
            if num in numDict:
                return True
            numDict[num] = 1
        return False
        
sol = Solution()
print(sol.containsDuplicate([1,2,3,4]))