'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

样例
输入：
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

输出：[1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution(object):
    def printMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix:
            return result
        row = len(matrix)
        column = len(matrix[0])
        x, y, cur_dir = 0, 0, 1
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        flag_matrix = [[False for _ in range(column)] for _ in range(row)]
        for _ in range(row * column):
            result.append(matrix[x][y])
            flag_matrix[x][y] = True
            a = x + dr[cur_dir]
            b = y + dc[cur_dir]
            if a < 0 or b < 0 or a >= row or b >= column or flag_matrix[a][b]:
                cur_dir = (cur_dir + 1) % 4
                a = x + dr[cur_dir]
                b = y + dc[cur_dir]
            x = a
            y = b
        return result

