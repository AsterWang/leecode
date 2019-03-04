'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

思路：从下往上处理，维护一个dp数组，数组中每一个slot是每一行的最小和

eg。

[
     [2],
    [3,4],
   [5,6,7],
]

dp = 	[0,0,0,0]  
	--> [5,6,7,0]  
	--> [min(8,9), min(10, 11), 7, 0], 这时我们选择minimal numer的那个，所以 --> [8, 10, 7, 0]
	--> [min(8+2, 10+2), 10, 7, 0] --> [10, 10, 7, 0]
'''
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        result = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                result[i] = row[i] + min(result[i], result[i + 1])
        return result[0]

S = Solution()
print(S.minimumTotal([[2],[3,4],[5,6,7]]))


