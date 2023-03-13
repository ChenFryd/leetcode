class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        intDict = {}
        for i in range(len(nums)):
            if (target-nums[i] in intDict):
                return [i,intDict[target-nums[i]]]
            intDict[nums[i]] = i
        return []
