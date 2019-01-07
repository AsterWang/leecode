class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def print_node(self, head):
    	while head:
    		print(head.val, end = '->')
    		head = head.next
    	print("============")

    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next
        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next
            # self.print_node(cur)

        print(cur.val)
        pre.next = reverse
        pre.next.next = cur
        return dummyNode.next


S = Solution()

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = None

S.reverseBetween(l1, 2, 4)


