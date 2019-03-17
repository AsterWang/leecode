# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def find_path(self, root, path, des):
        if not root:
            return False
        if root == des:
            path.append(root)
            return True

        #check if target node is either in the left subtree or right subtree
        find_left, find_right = False, False
        find_left = self.find_path(root.left, path, des)

        if not find_left:       #removing unnecessary check
            find_right = self.find_path(root.right, path, des)

        #if we found that the target node is not the current sub-tree,then we add current node to list
        if find_left or find_right:
            path.append(root)
        return find_right or find_left

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path_p = []
        path_q = []
        self.find_path(root, path_p, p)
        self.find_path(root, path_q, q)
        path_p.reverse()
        path_q.reverse()
        res = None
        for i in range(len(path_p)):

            #out of boundary, return
            if i >= len(path_q):
                return res
            #found shared node, move on
            if path_p[i] == path_q[i]:
                res = path_p[i]

            #we found first different node, return prior node
            if res and path_p[i] != path_q[i]:
                return res
        return res


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7

s = Solution()
res2 = s.lowestCommonAncestor(t1, t6, t5)
print(res2.val)
