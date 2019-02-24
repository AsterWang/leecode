'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''


#iterative solution
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        stack = []
        x = 1
        while True:
            length = len(stack)
            if length == k:
                result.append(stack[:])
            if length == k or x > n:
                if not stack:
                    return result
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1



#recursive solution
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs([i for i in range(1, n + 1)], k, 0,[], result)
        return result
    
    def dfs(self, nums, k, index, path, result):
        if k == 0:
            result.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, k - 1, i + 1, path + [nums[i]], result)