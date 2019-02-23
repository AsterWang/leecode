# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        root = head
        head = head.next
        while head:
            if head.val > root.val:
                tmp_head = root
                while root.next and head.val > root.val:
                    root = root.next
                root.next = head
                root = tmp_head
            else:
                tmp = root
                root = head
                root.next = tmp
            print(root.val)
            head = head.next
        return root

s = Solution()
l1 = ListNode(4)
l2 = ListNode(2)
l3 = ListNode(1)
l4 = ListNode(3)

l1.next = l2
l2.next = l3
l3.next = l4

root = s.insertionSortList(l1)
while root:
    print(root.val)
    root = root.next
