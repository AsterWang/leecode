'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

思路：
    同一个点不能被同一个路径两次，所以我们需要把路过的点设置为""。
    dfs遍历上下左右可能的路径，如果能把word的所有单词都遍历完，就返回True，只要有一个路径成立，就返回True
'''
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        N, M = len(board), len(board[0])
        for i in xrange(N):
            for j in xrange(M):
                if self.dfs(board, word, i, j):
                    return True
        return False
    
    def dfs(self, board, word, i, j):
        if board[i][j] == word[0]:  #speed up, compare the first character
            board[i][j] = ''
            if not word[1:]:
                return True
            if i > 0 and self.dfs(board, word[1:], i - 1, j):
                return True
            if i + 1 < len(board) and self.dfs(board, word[1:], i + 1, j):
                return True
            if j > 0 and self.dfs(board, word[1:], i, j - 1):
                return True
            if j + 1 < len(board[0]) and self.dfs(board, word[1:], i, j + 1):
                return True
            board[i][j] = word[0]
            return False
        else:
            return False