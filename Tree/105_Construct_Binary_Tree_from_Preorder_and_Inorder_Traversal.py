# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        d = deque(preorder)
        root = self.helper(d, inorder)
        return root
    def helper(self, d, inorder):
        if inorder:
            index = inorder.index(d.popleft())
            root = TreeNode(inorder[index])
            root.left = self.helper(d, inorder[:index])
            root.right = self.helper(d, inorder[index+1:])
            return root