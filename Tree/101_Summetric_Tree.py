'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        res = self.helper(root.left, root.right)
        return res

    # Recursive Solution
    def helper(self, left,right):
        if (left and not right) or (not left and right):
            return False
        if not left and not right:
            return True
        if left.val != right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)

    # Iterative Solution
    def helper_interative(self, root):
        if not root:
            return True
        left = root.left
        right = root.right
        left_stack, right_stack = [], []
        left_res, right_res = [], []
        while left or left_stack:
             if left:
                 left_res.append(left.val)
                 left_stack.append(left)
                 left = left.left
             else:
                left_res.append(None)
                left = left_stack.pop()
                left = left.right

        while right or right_stack:
            if right:
                right_res.append(right.val)
                right_stack.append(right)
                right = right.right
            else:
                right_res.append(None)
                right = right_stack.pop()
                right = right.left
        print(left_res)
        print(right_res)
        return left_res == right_res

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(2)
n4 = TreeNode(3)
n5 = TreeNode(4)
n6 = TreeNode(4)
n7 = TreeNode(3)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
s = Solution()
res = s.helper_interative(n1)
print(res)
print(s.isSymmetric(n1))
