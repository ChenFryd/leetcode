from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        output = []
        s = set()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                if sum == target:
                    s.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif sum < target:
                    j+=1
                else:
                    k-=1
        output = list(s)
        return output
    

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    s = Solution()
    print(s.threeSum(nums))