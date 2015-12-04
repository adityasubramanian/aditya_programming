# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        cur = head
        while cur != None: 
            length += 1
            curr = curr.next
        return self.mergeSort(head,length) 
    def MergeSort(self,head,length):
        if length == 1 or length ==0: 
            return head
        prev = curr = head 
        for i in xrange(length/2): 
            curr = curr.next
        