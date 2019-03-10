'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

Note:
    直接操作链表，merge sort，先局部有序再整体merge。首先对每个部分找到中点，然后对左半部分跟右半部分
    分别进行递归merge sort(divide and conquer)
'''
# Definition for singly-linked list.
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

        #base case, eg.None or length of linkedlist is 1
        if not head or not head.next:
            return head
        mid = self.find_mid(head)

        #sort right and left parts
        right = self.sortList(mid.next)
        mid.next = None             #disconnect the right part and left part to be individual part
        left = self.sortList(head)
        return self.merge(left, right)
    
    def find_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, head1, head2):
        dummy = ListNode(-1)
        head = dummy
        while head1 and head2:
            if head1.val < head2.val:
                dummy.next = head1
                head1 = head1.next
            else:
                dummy.next = head2
                head2 = head2.next
            dummy = dummy.next
        if head1:
            dummy.next = head1
        if head2:
            dummy.next = head2
        return head.next

l1 = ListNode(4)
l2 = ListNode(2)
l3 = ListNode(1)
l4 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = l4

s = Solution()
s.sortList(l1)
