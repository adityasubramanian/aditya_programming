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
            cur = cur.next
            length += 1 
        return self.mergeSort(head,length)

    def MergeSort(self,head,length):
        if length == 1 or length ==0: 
            return head
        prev = curr = head 
        for i in xrange(length/2): 
            curr = curr.next
<<<<<<< HEAD


            
        
=======
        #Not finished 
>>>>>>> 6601d951e0e97bee5c8fe6bcca5083a6f39ef9d4
