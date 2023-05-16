# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        currentNode = None
        carry = 0
        while l1 is not None or  l2 is not None or carry != 0:
            sum = carry
            carry = 0
            if (l1 is not None):
                sum += l1.val
                l1 = l1.next
            if (l2 is not None):
                sum += l2.val
                l2 = l2.next
            if (sum > 9 ):
                sum -= 10
                carry = 1
            newNode = ListNode(sum)
            if (head is None):
                head = newNode
            if (currentNode is not None):
                currentNode.next = newNode
            currentNode = newNode
        return head

# Test case
l1 = ListNode(1)
l1.next = ListNode(8)

l2 = ListNode(0)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Print the result
while result is not None:
    print(result.val, end=" ")
    result = result.next
