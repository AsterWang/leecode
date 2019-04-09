class Solution:
    def max_val(self, weights, values, w):
        dp = [[-1] * (w + 1) for _ in range(len(weight))]
        dp[0][0] = 0
        dp[0][weights[0]] = values[0]
        
        for i in range(1, len(weight)):
            # Not choose the ith item
            for j in range(w + 1):
                if dp[i - 1][j] >= 0:
                    dp[i][j] = dp[i - 1][j]
            
            # Choose the ith item
            for j in range(w - weights[i] + 1):
                if dp[i - 1][j] >= 0:
                    if dp[i - 1][j] + values[i] > dp[i][j + weights[i]]:
                        dp[i][j + weights[i]] = dp[i - 1][j] + values[i]
        return max(dp[-1])
    
    def max_val_one_dimension(self, weights, values, w):
        dp = [-1 for _ in range(w + 1)]
        dp[0] = 0
        dp[weight[0]] = values[0]

        for i in range(1, len(weight)):
            # Choose the ith item
            for j in range(w - weight[i], -1, -1):
                if dp[j] >= 0:
                    v = dp[j] + values[i] # the price of choosing the ith item
                    if dp[j + weight[i]] < v:
                        dp[j + weight[i]] = v
        print(dp)
        return max(dp)

s = Solution()
weight = [1, 3, 2]
val = [5, 4, 2]
res = s.max_val(weight, val, 5)
res2 = s.max_val_one_dimension(weight, val, 5)
print(res)
print(res2)