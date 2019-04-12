"""
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
"""

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        S = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    S.add((i,j))
        for s in S:
            if self.dfs(board,s,word):
                return True
        return False

    def dfs(self,board,coor,word):
        if len(word) == 0:
            return True
        if coor[0] < 0 or coor[0] >= len(board) or coor[1] < 0 or coor[1] >= len(board[0]) or word[0] != board[coor[0]][coor[1]]:
            return False
        char = board[coor[0]][coor[1]]
        board[coor[0]][coor[1]] = -1
        res = self.dfs(board,[coor[0]+1,coor[1]], word[1:]) \
              or self.dfs(board,[coor[0]-1,coor[1]], word[1:]) \
                or self.dfs(board,[coor[0],coor[1]+1], word[1:]) \
                or self.dfs(board,[coor[0],coor[1] - 1], word[1:])
        board[coor[0]][coor[1]] = char
        return res


board =[
  ['A','B'],
  ['C','D']
]

word = 'ABCD'

S = Solution()
print(S.exist(board,word))
 
        		





