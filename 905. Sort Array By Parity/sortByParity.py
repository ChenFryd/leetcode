from typing import List 
class Solution:
    def sortArrayByParity(self, nums: List[int]):
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1]