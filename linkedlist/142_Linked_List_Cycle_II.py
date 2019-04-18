'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the 
position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in 
the linked list.

Note: Do not modify the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

slow : a + b
fast : a + b + c + b
fast = 2 * slow
   => 2*(a + b) = a + b + c + b
   => a = c
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        slow = fast = head
        flag = False
        while fast and slow:
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            if slow == fast:
                flag = True
                break
        if flag:
            while slow != head:
                slow = slow.next
                head = head.next
            return head
        return None
