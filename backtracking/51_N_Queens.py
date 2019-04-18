class Solution:

    def solveNQueens(self, n):
        result = []
        nums = [-1] * n
        self.dfs(nums, [], 0, result)
        for x in result:
            print(x)
        return result

    def is_valid(self,nums,  queen_no):
        for i in range(queen_no):
            if nums[i] == nums[queen_no] or queen_no - i == abs(nums[i] - nums[queen_no]):
                return False
        return True

    def dfs(self, nums, path, queen_no, result):
        if queen_no == len(nums):
            result.append(path)
            return
        for i in range(len(nums)):
            nums[queen_no] = i
            if self.is_valid(nums, queen_no):
                tmp = '#' * len(nums)
                self.dfs(nums, path + [tmp[:i] + 'Q' + tmp[i+1:]], queen_no + 1, result)

S = Solution()
S.solveNQueens(6)
