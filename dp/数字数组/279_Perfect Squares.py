'''
dp[0] = 0
dp[1] = dp[0] + 1 = 1
dp[2] = dp[1] + 1 = 2
dp[3] = dp[2] + 1 = 3
dp[4] = min(dp[4-1*1] + 1, dp[4-2*2]+1)
      = min(dp[3]+1, dp[0]+1) = 2
dp[5] = min(dp[5-1*1]+1, dp[5-2*2]+1)
      = min(dp[4]+1, dp[1]+1) = 2
    ...
    ...
dp[n] = min(dp[n-1*1]+1, dp[n-2*2]+1, dp[n-3*3]+1,...)
'''
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 1
        res = 0
        for i in range(1, n + 1):
            tmp = math.sqrt(i)
            tmp = int(tmp)
            if tmp * tmp == i:
                dp[i] = 1
                continue
            for j in range(1, tmp + 1):
                rest = i - j * j
                dp[i] = min(dp[i], dp[rest] + 1)
        return dp[-1]