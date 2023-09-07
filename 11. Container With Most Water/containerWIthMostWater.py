from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) -1
        maxArea = 0

        while left < right:
            maxArea = max(maxArea, (right-left)*min(height[left],height[right]))
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        
        return maxArea

sol = Solution()
print(sol.maxArea([1,3,2,4]))