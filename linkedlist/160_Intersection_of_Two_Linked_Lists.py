'''
Write a program to find the node at which the intersection of two singly linked lists begins.

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        l1, l2 = 0,0
        tmpA = headA
        tmpB = headB
        while tmpA:
            l1 += 1
            tmpA = tmpA.next
        while tmpB:
            l2 += 1
            tmpB = tmpB.next
        rest = abs(l1 - l2)
        if l1 > l2:
            for _ in range(rest):
                headA = headA.next
        elif l1 < l2:
            for _ in range(rest):
                headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA