'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp = head
        length = 0
        while head:
            length +=1 
            head = head.next
        dummy = ListNode(-1)
        dummy.next = tmp
        head = dummy
        rest = length - n
        while rest:
            rest -=1
            head = head.next
        head.next = head.next.next
        return dummy.next
            
            
        