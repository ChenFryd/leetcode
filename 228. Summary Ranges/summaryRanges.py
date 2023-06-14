from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        lastNumIndex = 0
        for i in range(1,len(nums)):
            if nums[i]-1 != nums[i-1]:
                if i-lastNumIndex == 1:
                    output.append(f"{nums[lastNumIndex]}")
                else:
                    output.append(f"{nums[lastNumIndex]}->{nums[i-1]}")
                lastNumIndex = i
        if len(nums) > 0:
            if len(nums)-lastNumIndex == 1:
                output.append(f"{nums[lastNumIndex]}")
            else:
                output.append(f"{nums[lastNumIndex]}->{nums[-1]}")
        return output

sol = Solution()
print(sol.summaryRanges([0,1,2,4,5,7]))                