# -*- coding: utf-8 -*-
'''
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

假设字符串中只包含从’a’到’z’的字符。

样例
输入："abcabc"

输出：3
'''
class Solution:
    def longestSubstringWithoutDuplication(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0
        d = {}
        begin = 0
        mx = 0
        for i, n in enumerate(s):
            d[n] = d.get(n, 0) + 1
            while d[n] > 1:
                d[s[begin]] -=1
                begin +=1
            mx = max(mx, i - begin + 1)
        return mx
