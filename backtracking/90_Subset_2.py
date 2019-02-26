class Solution(object):
    # DFS  
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            if i > index and nums[i] == nums[i-1]: # i > index 确保目前遍历的这个数是在之前遍历的那个数之后，之前的数是已经被dfs过了。
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)

s = Solution()
s.subsetsWithDup([1,2,2])
