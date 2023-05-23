class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        lastChar = nums[0]
        numDuplicate = 0
        while i+numDuplicate < len(nums):
            if nums[i] == lastChar:
                for j in range (i+1,len(nums)):
                    nums[j-1] = nums[j]
                numDuplicate += 1
            else:
                lastChar = nums[i]
                i += 1
            
        return len(nums) - numDuplicate
    
sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))