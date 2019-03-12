'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

note: 
    1.find the partially maximum and partially minimum
    2.consider when the maximum and minimum will be changed.
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        res = nums[0]
        mx = nums[0]
        mi = nums[0]
        res = nums[0]
        for i in range(1, length):
            tmp = mx
            mx = max(mi * nums[i], nums[i], mx * nums[i])
            mi = min(mi * nums[i], nums[i], tmp * nums[i])
            res = max(res, mx)
        return res