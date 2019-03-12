'''
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

NOTE:
    Each element id DP array need to store two things:
        1) The largest length of subsequence ending at this index
        2) Number of longest length of subsequences by this index
'''
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [(1,1)] * len(nums)
        mx_length = 1
        for i, num in enumerate(nums):
            length, count = 1, 0
            for j in range(i):
                if num > nums[j]:
                    if dp[j][0] + 1 > length:
                        length = dp[j][0] + 1
                        count = 0
                    if dp[j][0] + 1 == length:
                        count += dp[j][1]
            mx_length = max(mx_length, length)
            dp[i] = (length, max(count, 1))
        return sum(item[1] for item in dp if item[0] == mx_length)