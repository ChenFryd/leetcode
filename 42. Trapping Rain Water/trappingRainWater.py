from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        sum = 0
        index = 1
        stack = [height[0]]
        while index < len(height):
            while height[index] >= stack[-1]:
                sum += min(height[index], stack.pop())
            stack.append(height[index])
            index += 1
        return sum
    
sol = Solution()
print(sol.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))