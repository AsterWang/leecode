'''
输入一棵二叉树的根结点，判断该树是不是平衡二叉树。

如果某二叉树中任意结点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

注意：

规定空树也是一棵平衡二叉树。
样例
输入：二叉树[5,7,11,null,null,12,9,null,null,null,null]如下所示，
    5
   / \
  7  11
    /  \
   12   9

输出：true

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        #get the depth of left substree and right subtree
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        #if depth difference larger than 1, return False
        if abs(left - right) > 1:
            return False
        #Otherwise, moving on
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def dfs(self, root):
        if not root:
            return 0
        left_depth = self.dfs(root.left)
        right_depth = self.dfs(root.right)
        return max(left_depth, right_depth) + 1

