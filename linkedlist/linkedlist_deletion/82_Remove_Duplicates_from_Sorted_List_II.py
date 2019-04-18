'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

思路：
    1）创建三个指针，ppre, pre, cur， ppre记录的是前一个没有重复元素的位置，pre与cur对元素的重复性进行判断，如果有重复，则一直往后遍历。
    2）需要注意的是：如果head的元素是重复的，则需要重新设置head的位置，指向重复元素的下一个元素。
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        ppre = head
        pre = head
        cur = head
        tmp_head = head
        if pre:
            cur = pre.next
        while cur:
            if cur.val == pre.val:
                while cur and cur.val == pre.val:
                    pre = cur
                    cur = cur.next
                
                #case like 1->1->1
                if ppre.val == pre.val:         #reset head position
                    tmp_head = cur
                    ppre = cur
                #case like 1->2->2->2
                else:
                    ppre.next = cur
                pre = cur
                if pre:
                    cur = pre.next
            else:
                ppre = pre
                pre = cur
                cur = cur.next
        return tmp_head
    