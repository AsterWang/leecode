'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Note:
    1.每一个slot能获得的最长的正方形的边长度需要考虑dp[i-1][j],dp[i][j-1] 和 d[i-1][j-1]
    2.增加dummy列与dummy行，这样可以把第一行跟第一列的情况考虑进去
'''
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        r, c = len(matrix), len(matrix[0])
        #考虑第一行或者第一列的情况，可以增加一行dummy跟一列dummy
        dp = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
        res = 0
        for i in range(1, r+1):
            for j in range(1, c+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                    res = max(res, dp[i][j])
        return res * res