class Solution:
    def minimum_path(self, arr):
        length = len(arr)
        dp = [[0] * length for _ in range(length)]
        dp[0][0] = arr[0][0]

        for i in range(1, length):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + arr[i][j]
                elif j == i:
                    dp[i][j] = dp[i - 1][j - 1] + arr[i][j]
                else:
                    dp[i][j] = arr[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j])
            print(dp[i])
        return min(dp[-1])

s = Solution()
arr = [[5],[7,8],[2,3,4],[4,9,6,1], [2,7,9,4,5]]
res = s.minimum_path(arr)
print(res)