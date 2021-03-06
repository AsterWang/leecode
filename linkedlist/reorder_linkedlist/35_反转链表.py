'''

定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点。

样例
输入:1->2->3->4->5->NULL

输出:5->4->3->2->1->NULL

#None <- 1
        #1 <-2
        #1 <-2 <- 3
        #1 <-2 <- 3 <-4 <- 5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = None
        while head:
            tmp = head
            head = head.next
            tmp.next = dummy
            dummy = tmp
        return dummy