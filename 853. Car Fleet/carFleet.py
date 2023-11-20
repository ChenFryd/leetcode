from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

            

            
            
sol = Solution() 
print(sol.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])) # 3
print(sol.carFleet(10, [6,8], [3,2])) # 2
print(sol.carFleet(10, [0,4,2], [2,1,3])) # 1
print(sol.carFleet(10, [0,2,4], [2,1,3])) # 2
print(sol.carFleet(10, [0,2,4], [2,1,0])) # 1
print(sol.carFleet(10, [0,2,4], [2,1,1])) # 225