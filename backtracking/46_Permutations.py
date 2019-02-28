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

思路：
    what we need to consider is that the number is in the number set and not been looped yet.
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
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], result)

s = Solution()
result = s.permute(['c', 'a', 't', 'd', 'o', 'g'])
print(len(result))