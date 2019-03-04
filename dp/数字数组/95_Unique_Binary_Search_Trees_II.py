# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.dfs([i for i in range(1, n + 1)])

    def dfs(self, nums):
        if not nums:
            return [None]
        res = []

        #as for different number, we could generate a list of left tree and a list of right tree
        #then produce the combination of left tree and right tree.
        for i in range(len(nums)):
            #generate left tree
            left_tree = self.dfs(nums[:i])
            #generate right tree
            right_tree = self.dfs(nums[i+1:])
            for left in left_tree:
                for right in right_tree:
                    father = TreeNode(nums[i])
                    father.left = left
                    father.right = right
                    res += [father]
        return res

s = Solution()
s.generateTrees(3)
