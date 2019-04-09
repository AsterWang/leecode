'''
将一对有重量的物品装入固定容量的背包，使得背包中的重量最大。
'''
class Solution:
    def max_weight(self, nums, w):
        dp = [[False] * (w + 1)for _ in range(len(nums))]
        dp[0][0] = True
        dp[0][nums[0]] = True
        for i in range(1, len(nums)):
            #not put in the ith item
            for j in range(w):
                if dp[i - 1][j]:
                    dp[i][j] = True
            #put in the ith item
            for j in range(w - nums[i] + 1):
                if dp[i - 1][j]:
                    dp[i][j + nums[i]] = True
        for x in range(w, -1, -1):
            if dp[-1][x]:
                return x
        return 0
    
    def max_weight_one_dimension(self, nums, w):
        dp = [False for _ in range(w + 1)]
        dp[0] = True
        dp[nums[0]] = True
        for i in range(1, len(nums)):
            for j in range(w - nums[i] + 1):
                if dp[j]:
                    dp[j + nums[i]] = True
        for x in range(w, -1, -1):
            if dp[x]:
                return x
        return 0

s = Solution()
L = [2,2,4,6,2]
res = s.max_weight(L, 7)
res2 = s.max_weight_one_dimension(L, 7)
print(res)
print(res2)


