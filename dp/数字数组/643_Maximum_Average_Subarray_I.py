'''
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 

Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

思路：
    1）维护一个length = 4 的 sliding window, pop the first element in this window whenever moving
    2) 计算出到当前位置的总和

'''
class Solution(object):
    #SLIDING WINDOW
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_val = float('-inf')
        sum = 0
        for i, num in enumerate(nums,1):
            sum += num
            if i > k:
                sum -= nums[i-k-1]
            if i >= k:
                max_val = max(max_val, sum)
        return float(max_val) / k
    
    #DP
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum_list = [0]
        for num in nums:
            sum_list.append(sum_list[-1] + num)
        max_val = max(sum_list[i + k] - sum_list[i] for i in range(len(nums) - k + 1))
        return max_val / float(k)

            
        