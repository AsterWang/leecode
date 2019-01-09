'''
从上往下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印。

样例
输入如下图所示二叉树[8, 12, 2, null, null, 6, null, 4, null, null, null]
    8
   / \
  12  2
     /
    6
   /
  4

输出：[8, 12, 2, 6, 4]

算法：
    1.  我们从root开始按照bfs（宽度优先） 顺序遍历整棵树，首先访问left child， 然后是right child
    2.  然后在从左到右扩展第三层节点
    3.  一次类推

    时间复杂度
        BFS时每个节点仅被遍历一次，所以时间复杂度是 O(n)O(n)。
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def printFromTopToBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = [root.val]
        tmp = [root]
        while len(tmp) != 0:
            top = tmp.pop(0)
            if top.left:
                tmp.append(top.left)
                result.append(top.left.val)
            if top.right:
                tmp.append(top.right)
                result.append(top.right.val)
        return result
        