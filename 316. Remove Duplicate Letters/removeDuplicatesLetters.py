from collections import defaultdict
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        stack = []
        vis = set()
        for char in s:
            d[char] -= 1
            if char in vis:
                continue
            while stack and d[stack[-1]] >= 1 and stack[-1] > char:
                vis.remove(stack.pop())
            vis.add(char)
            stack.append(char)
        return "".join(stack)