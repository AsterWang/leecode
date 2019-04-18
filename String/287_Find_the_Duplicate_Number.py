'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3

NOTE:
eg [1,3,4,2,2]
我们采用第一种策略：                       如果采用第二种策略：
t = nums[0] = 1                         t = nums[nums[t]] = 3
t = nums[1] = 3                         t = nums[nums[t]] = 4
t = nums[3] = 2                         t = nums[nums[t]] = 4
t = nums[2] = 4                         ....
t = nums[4] = 2                         我们发现进入了一个循环
t = nums[2] = 4
...
我们可以发现进入了一个循环

其实我们可以发现第二种策略就是第一种策略所用的步伐的两倍，可以想象成这个数组是一个带环的链表组成，
当进入链表中的一个环时，快慢指针总会在某个点相遇。当相遇的时候退出（跟leetcode 142的链表环一样）。
'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = 0
        finder = 0
        while True:
            slow = nums[slow] #每次走一步
            fast = nums[nums[fast]] #每次走两步
            if slow == fast: #如果快慢指针相遇，退出
                break

        #从起点开始走，直到找到环的入口位置
        while True:
            slow = nums[slow]
            finder = nums[finder] 
            if slow == finder:
                return slow