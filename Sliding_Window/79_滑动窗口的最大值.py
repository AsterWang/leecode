# -*- coding: utf-8 -*-
'''
给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。

例如，如果输入数组[2, 3, 4, 2, 6, 2, 5, 1]及滑动窗口的大小3,那么一共存在6个滑动窗口，它们的最大值分别为[4, 4, 6, 6, 6, 5]。

注意：

数据保证k大于0，且k小于等于数组长度。
样例
输入：[2, 3, 4, 2, 6, 2, 5, 1] , k=3

输出: [4, 4, 6, 6, 6, 5]
'''
from collections import deque
class Solution(object):
    def maxInWindows(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = deque()
        res = []
        for i, n in enumerate(nums):
            while d and n > nums[d[-1]]:
                d.pop()
            d.append(i)
            if d[0] <= i - k:
                d.popleft()
            if i >= k - 1:
                res.append(nums[d[0]])
        return res
