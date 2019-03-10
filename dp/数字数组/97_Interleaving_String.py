'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

思路:
    dp[i][j]表示的是s1[:i+1]和s2[:j+1]能够交替形成s3[:i+j+1]
    判断dp[i][j]是否可行，可以判断
        1) s1[i] == s3[i+j] and dp[i-1][j] == True
        2) s2[j] == s3[i+j] and dp[i][j-1] == True
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3 : str) -> bool:
        r, c, l= len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        dp = [[True for _ in range(c+1)] for _ in range(r+1)]
        for i in range(1, r + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i-1]
        for j in range(1, c + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j-1]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or \
               (dp[i][j-1] and s2[j-1] == s3[i-1+j])
        return dp[-1][-1]