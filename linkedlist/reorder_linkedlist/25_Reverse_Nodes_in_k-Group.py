# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        stack = []
        while cur:
            for _ in range(k):
                if not cur:
                    break
                stack.append(cur)
                cur = cur.next
            if len(stack) != k:
                return dummy.next
            else:
                next_node = stack[-1].next
                for _ in range(k):
                    node = stack.pop()
                    pre.next = node
                    pre = pre.next
                pre.next = next_node
            cur = next_node
        return dummy.next