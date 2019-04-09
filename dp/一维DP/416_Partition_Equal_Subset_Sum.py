class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2:
            return False 
        half = s // 2
        dp = [False for _ in range(half + 1)]
        dp[0] = True
        length = len(nums)
        for i in range(1, length + 1):
            for j in range(half, nums[i - 1] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i - 1]]
        return dp[-1]