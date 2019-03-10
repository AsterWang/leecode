'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        mid = self.cut_linkedlist(head)
        reverse = self.reverse_linkedlist(mid)
        head = self.merge_two_linkedlist(head, reverse)
        
    def merge_two_linkedlist(self, head1, head2):
        dummy = ListNode(-1)
        head = dummy
        print(head1.val, head2.val)
        while head1 and head2:
            tmp1 = head1.next
            tmp2 = head2.next
            head.next = head1
            head.next.next = head2
            head1 = tmp1
            head2 = tmp2
            head = head.next.next
        if head1:
            head.next = head1
        if head2:
            head.next = head2
        return dummy.next            
        
    def reverse_linkedlist(self, head):
        dummy = None
        while head:
            tmp = head
            head = head.next
            tmp.next = dummy
            dummy = tmp
        return dummy
    
    def cut_linkedlist(self, head):
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow.next
        slow.next = None
        return middle
            