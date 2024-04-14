from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path):
            if not nums:
                result.append(tuple(path))
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:],path+[nums[i]])
        result = set()
        backtrack(nums,[])
        return result
    
# Create an instance of the Solution class
s = Solution()

# Test the permute() method
nums = [1, 1, 2]
result = s.permuteUnique(nums)
print(result)