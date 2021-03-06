# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.dfs(root)
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.right)
        self.dfs(root.left)
        root.left = None
        root.right = self.prev
        self.prev = root

node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)

node_1.left = node_2
node_1.right = node_5
node_2.left = node_3
node_2.right = node_4
node_5.right = node_6


S = Solution()
S.flatten(node_1)

