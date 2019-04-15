# Definition for a binary tree node.
'''
给定一棵二叉搜索树，请找出其中的第k小的结点。

你可以假设树和k都存在，并且1≤k≤树的总结点数。

样例
输入：root = [2, 1, 3, null, null, null, null] ，k = 3

    2
   / \
  1   3

输出：3
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = None
        self.k = 0
    def preOrder(self, root):
        if not root:
            return
        self.preOrder(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root
            return
        self.preOrder(root.right)


    def kthNode(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: TreeNode
        """
        self.k = k
        self.preOrder(root)
        return self.res

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
res = s.kthNode(t4, 4)
print(res.val)
