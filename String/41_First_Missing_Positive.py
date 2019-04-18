'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

NOTE:
    Index   0   1   2   3
    num     3   4   -1  1
     =>     -1  4   3   1
     =>     -1  1   3   4
     =>     1   -1  3   4

     最后：遍历数组，如果 i + 1 != nums[i], return i + 1
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            while 0 <= nums[i] - 1 < length and nums[i] != nums[nums[i] - 1]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        
        for i in xrange(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1