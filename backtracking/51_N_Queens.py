class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        nums = [-1] * n
        self.dfs(nums, [], 0, result)
        return result
    
    def dfs(self, nums, path, pos, result):
        if pos == len(nums):
            result.append(path)
            return
        
        #which column is the possible slot for avoiding attack
        for i in range(len(nums)):
            nums[pos] = i           #set the No.pos queen to the ith column 
            if self.is_valid(nums, pos):
                tmp = '.' * len(nums)
                self.dfs(nums, path + [tmp[:i] + 'Q' + tmp[i+1:]], pos + 1, result)
    def is_valid(self, nums, pos):
        for i in range(pos):
            # k = +1 or k = -1, which means x - x1 = abs(y - y1)
            if nums[pos] == nums[i] or abs(nums[pos] - nums[i]) == pos - i:
                return False
        return True