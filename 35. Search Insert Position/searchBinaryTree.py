from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start,end = 0,len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            start,end = (start,mid-1) if target<nums[mid] else (mid+1,end)
        return start

sol = Solution()
print(sol.searchInsert([1,3,5,6],2))
print(sol.searchInsert([1,3,5,6],7))
print(sol.searchInsert([1,3,5,6],0))
print(sol.searchInsert([1,3,5,6],1))