# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 or l2) is None:
            return l1 if l2 is None
        return l2
        placement = ListNode(0) 
        while (l1 and l2) is not None: 
            placement.next = ListNodE((l1.val+l2.val) 
            flag = (l1.val + l2.val)/10 
            
        if flag is None: 
            return