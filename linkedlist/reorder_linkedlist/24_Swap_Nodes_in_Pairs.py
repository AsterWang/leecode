# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        while cur and cur.next:
            tmp = cur.next.next
            pre.next = cur.next
            pre.next.next = cur
            cur.next = tmp
            pre = cur
            cur =tmp
        return dummy.next