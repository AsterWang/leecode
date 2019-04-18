'''
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes 
in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges 
between them.

NOTE:   # This path may or may not pass through the root, so every time we get 
        # the max depth of left subtree and right subtree, we need to compare 
        # the sum of them with current max length
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        # Since we need to count the number of edge, so return 0.
        # If we need to get the max depth of a subtree, return 1 
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res = max(self.res, left + right)
        return 1 + max(left, right)
        