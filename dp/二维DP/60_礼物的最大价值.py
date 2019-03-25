# -*- coding: utf-8 -*-
'''
在一个m×n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。

你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格直到到达棋盘的右下角。

给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？

注意：

m,n>0
样例：

输入：
[
  [2,3,1],
  [1,7,1],
  [4,6,1]
]

输出：19

解释：沿着路径 2→3→7→6→1 可以得到拿到最大价值礼物。
'''
class Solution(object):
    def getMaxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        dp = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r+1):
            for j in range(1, c+1):
                dp[i][j] = grid[i-1][j-1] + max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
        