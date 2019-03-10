class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = 0
        nums_list = list(nums)
        self.dfs(nums_list, [], 0)
        return self.result
    
    def dfs(self, nums, path, count):
        if not nums:
            self.result += 1
            return
        length = len(nums)
        for i in range(length):
            if path and nums[i] != path[-1]:
                if count > 0:
                    continue
                else:
                    self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], count + 1)
            else:
                self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], count)
str = "ABAB"
s = Solution()
result = s.permuteUnique(str)
print(result)
