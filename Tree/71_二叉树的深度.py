# -*- coding: utf-8 -*-
'''
输入一棵二叉树的根结点，求该树的深度。

从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

样例
输入：二叉树[8, 12, 2, null, null, 6, 4, null, null, null, null]如下图所示：
    8
   / \
  12  2
     / \
    6   4

输出：3
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def treeDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.dfs(root.left), self.dfs(root.right))
    def dfs(self, root):
        if not root:
            return 1
        return max(1 + self.dfs(root.left), 1 + self.dfs(root.right))

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)

t4.left = t2
t2.left = t1
t2.right = t3
t4.right = t5
t5.left = t6
t5.right = t7

s = Solution()
res = s.treeDepth(t4)
print(res)
