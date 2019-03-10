'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

workbook:
    1.initial state

    2.stack transfermation
        1) current number is 0, then it need to combine with prior number(check validation of combination)
        2) current number is not 0
            1.current number = 1,2,3,4,5,6 
                ==> current number can be an individual or combined with prior number
                ==> dp[i] = dp[i - 1] + dp[i - 2]
            2.current number = 7,8,9
                ==> current number must be an individual number
                ==> dp[i] = dp[i - 1]
                
    3.result 
'''
class Solution:
    def numDecodings(self, s):
        if len(s) == 0 or s.startswith('0'):return 0
        pre = 1
        cur = 1
        for i in range(1, len(s)):
            #if s[i] == '0', we need to check the validation of prior number
            tmp = cur
            if s[i] == '0':
                print("case1")
                #if current number is 0, then it must combine with prior number,
                #in this case, dp[i] = dp[i - 1]==> cur = pre
                if s[i - 1] == '0' or s[i - 1] > '2':return 0
                cur = pre
            else:
                #if 1 <= s[i-1]s[i] <= 26, then current number can be an individual number or combine with prior number, that means dp[i] = dp[i-1] + dp[i-2]
                if s[i - 1] != '0' and s[i-1:i+1] <= '26':
                    cur += pre
            pre = tmp
        return cur
        
