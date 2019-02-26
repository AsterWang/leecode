'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

思路：
    1.确定valid number，我们不仅需要确定这个数在数组中，还要确定这个数没有被用过。
    2.所以，我们先对数组进行sort，如果nums[i] == nums[i - 1],说明下一个数是invalid number，就continue跳过这个数。
'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        self.dfs(nums, [], result)
        return result
    
    def dfs(self, nums, path, result):
        if not nums:
            result.append(path)
            
        length = len(nums)
        for i in xrange(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], result)
        