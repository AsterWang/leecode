'''
输入一个二叉树，将它变换为它的镜像。

样例
输入树：
      8
     / \
    6  10
   / \ / \
  5  7 9 11

 [8,6,10,5,7,9,11,null,null,null,null,null,null,null,null] 
输出树：
      8
     / \
    10  6
   / \ / \
  11 9 7  5

 [8,10,6,11,9,7,5,null,null,null,null,null,null,null,null]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mirror(self, root):
        """
        :type root: TreeNode
        :rtype: void
        """
        if not root:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.mirror(root.left)
        self.mirror(root.right)