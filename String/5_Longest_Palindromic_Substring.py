'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        string = ''
        length = len(s)
        for i in range(length):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(string):
                string = tmp
            
            tmp2 = self.helper(s, i, i + 1)
            if len(tmp2) > len(string):
                string = tmp2
        return string
    
    def helper(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1 : j]