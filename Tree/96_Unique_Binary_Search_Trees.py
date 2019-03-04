'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

DP:
    n = 3
    /  \
    0   1
    1   2
    2   0

当 number = n 时，L = [0,1,2,...,n]，list中每个number都可以作为root，不同的number作为root，对应的左右子树节点个数不同，
例如当
    root = 2，  (#left_tree = 1, #right_tree = 0) or (#left_tree = 1, #right_tree = 0)
    root = 3,   (#left_tree = 2, #right_tree = 0) or (#left_tree = 1, #right_tree = 1) or (#left_tree = 0, #right_tree = 2)
所以
    1）初始化状态, result = [1,1,0,0,0,...,0], size = n + 1
    2）状态转移方程 : h(n) = h(0)*h(n-1) + h(1)*h(n-2) + ... + h(n-1)h(0) (其中n>=2, h(0) = h(1) = 1)
    3) 结果 = result[n]
'''
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        result = [0] * (n + 1)
        result[0] = 1
        result[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                result[i] += result[j] * result[i -1 -j]
        return result[n]