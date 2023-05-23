class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        l =1
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                nums[l] = nums[j]
                l += 1

        return l
    

sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))