'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(nums, [], result)
        return result
    
    def dfs(self, nums, path , result):
        if not nums:
            result.append(path)
            return
        for i in xrange(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], result)