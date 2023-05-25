class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = 0
        if nums == []:
            return l
        for i in range(0,len(nums)):
            nums[l] = nums[i]
            if nums[i] != val:
                l += 1
        return l

sol = Solution()
print (sol.removeElement([3,2,2,3],2))