# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findPath(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(root, [], sum)
        return self.res
    def dfs(self, root, path, sum):
        if not root or sum < 0:
            return
        if not root.left and not root.right and sum == root.val:
            self.res.append(path + [root.val])
            return
        self.dfs(root.left, path + [root.val], sum - root.val)
        self.dfs(root.right, path + [root.val], sum - root.val)

n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(6)
n4 = TreeNode(12)
n5 = TreeNode(13)
n6 = TreeNode(6)
n7 = TreeNode(9)
n8 = TreeNode(1)
n9 = TreeNode(5)
n10 = TreeNode(1)

n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n5
n3.right = n6
n4.left = n7
n4.right = n8
n6.left = n9
n6.right= n10
s = Solution()
res = s.findPath(n1, 22)
print(res)