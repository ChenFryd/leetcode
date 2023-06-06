from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = arr.sort()
        for i in range(1, len(arr) - 1):
            if arr[i] - arr[i - 1] != arr[i + 1] - arr[i]:
                return False
        return True
    
sol = Solution()
print(sol.canMakeArithmeticProgression([3,5,1]))
print(sol.canMakeArithmeticProgression([1,2,4]))
print(sol.canMakeArithmeticProgression([1,2,3,4,5,6,7,8,9,10]))