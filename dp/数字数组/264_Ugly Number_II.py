'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
'''
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ix2 = ix3 = ix5 = 0
        u2, u3, u5 = 2, 3, 5
        dp = [1]
        while n > 1:
            u2, u3, u5 = 2 * dp[ix2], 3 * dp[ix3], 5 * dp[ix5]
            temp_min = min(u2, u3, u5)
            if temp_min == u2:
                ix2 +=1
            if temp_min == u3:
                ix3 += 1
            if temp_min == u5:
                ix5 += 1
            dp.append(temp_min)
            n -= 1
        return dp[-1]