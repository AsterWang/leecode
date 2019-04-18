"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

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
"""

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
        if board[i][j] == word[0]:
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
        
board =[
  ['A','B'],
  ['C','D']
]

word = 'ABCD'

S = Solution()
print(S.exist(board,word))
 
        		





