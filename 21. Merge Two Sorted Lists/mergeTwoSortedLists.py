#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = None
        currentNode = None
        while (list1 is not None or list2 is not None):
            val1 = list1.val if list1 is not None else 200
            val2 = list2.val if list2 is not None else 200
            node = ListNode(val1) if val1<val2 else ListNode(val2)
            list1 = list1.next if val1<val2 else list1
            list2 = list2.next if val1>=val2 else list2
            if head is None:
                head = node
                currentNode = node
            else:
                currentNode.next = node
                currentNode = currentNode.next
        return head
            
sol = Solution();
list1 = ListNode(1,ListNode(2,ListNode(4)))
list2 = ListNode(1,ListNode(3,ListNode(4)))

noutputList = sol.mergeTwoLists(list1,list2)
while (outputList is not None):
    print(outputList.val)
    outputList = outputList.next