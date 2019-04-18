'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''
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
        self.helper(root)
    
    def helper(self, root):
        if not root:
            return None
        self.helper(root.right)
        self.helper(root.left)
        root.left = None
        root.right = self.prev
        self.prev = root

n1 = TreeNode(1)
n2 = TreeNode(2)
n5 = TreeNode(5)
n3 = TreeNode(3)
n4 = TreeNode(4)
n6 = TreeNode(6)

n1.left = n2
n1.right = n5
n5.left = n3
n5.right = n6
n2.right = n4
s = Solution()
s.flatten(n1)
