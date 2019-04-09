class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = 0
        nums_list = list(nums)
        self.dfs(nums_list, [], 0, result)
        return result
    
    def dfs(self, nums, path, count, result):
        if not nums:
            result += 1
            print(result)
            return
        length = len(nums)
        for i in range(length):
            if path and nums[i] != path[-1]:
                if count > 0:
                    continue
                else:
                    self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], count + 1, result)
            else:
                self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], count, result)


str = "ABAB"
s = Solution()
result = s.permuteUnique(str)
print(result)
