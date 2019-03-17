'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(nums, 0, [], result)
        return result
    
    def dfs(self, nums, index, subset, result):
        result.append(subset)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i + 1, subset + [nums[i]], result)

S = Solution()
print(S.subsets([1,2,3]))