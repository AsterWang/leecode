# 将一个骰子投掷n次，获得的总点数为s，s的可能范围为n~6n。
#
# 掷出某一点数，可能有多种掷法，例如投掷2次，掷出3点，共有[1,2],[2,1]两种掷法。
#
# 请求出投掷n次，掷出n~6n点分别有多少种掷法。
#
# 样例1
# 输入：n=1
#
# 输出：[1, 1, 1, 1, 1, 1]
#
# 解释：投掷1次，可能出现的点数为1-6，共计6种。每种点数都只有1种掷法。所以输出[1, 1, 1, 1, 1, 1]。
# 样例2
# 输入：n=2
#
# 输出：[1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
#
# 解释：投掷2次，可能出现的点数为2-12，共计11种。每种点数可能掷法数目分别为1,2,3,4,5,6,5,4,3,2,1。
#
#       所以输出[1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]。
class Solution(object):
    def numberOfDice(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        columns = 6*n + 1
        dp = [[0 for _ in range(columns)] for _ in range(n + 1)]
        #first try must between 1 - 6
        for j in range(1, 7):
            dp[1][j] = 1
        for i in range(2, n+1):
            for j in range(i*6, i-1, -1):
                for x in range(1, 7):
                    if j - x >= 0:
                        dp[i][j] += dp[i-1][j-x]
        return dp[-1][n:6*n+1]
