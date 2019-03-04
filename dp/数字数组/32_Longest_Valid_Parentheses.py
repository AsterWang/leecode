'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

思路：当str[i] ==')'时，index = i处最大的连续子串可以理解为：是以index = i 为最右端的最长括号匹配连续子序列
     dp[i]的求法：
        1）s[i] = '(',  那么dp[i] = 0
        2) s[i] = ')',  那么我们要关注的index是 j = i - dp[i - 1] - 1，如果s[j] == '('，那说明跟当前的')'匹配上
           ，则dp[i] = dp[i - 1] + 2。

    需要注意的是：在 s[:j]的子串里，可能会有已经匹配上的子串，所以在算出dp[i]后，我们还需要加上dp[j - 1]的值。例如
                ( ) ( ( ) )  
        index   0 1 2 3 4 5  ==> 我们可以看到index = 5 如果没有加上dp[j - 1]的值，结果是4，也就是我们没有考虑上s[:j]区域的匹配数。
        dp      0 2 0 0 2 6      所以，我们必须考虑上dp[j - 1]的值，也就是dp[i] += dp[j - 1]
'''

class Solution:
    def longestValidParentheses(self, s):
        if not s:
            return 0
        length = len(s)
        dp = [0] * length
        for i in range(1, length):
            if s[i] == ')':
                j = i - 1 - dp[i - 1]
                if j >= 0 and s[j] =='(':
                    dp[i] = dp[i - 1] + 2
                    if j - 1 > 0:
                        dp[i] += dp[j - 1]
        return max(dp)
