'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        pointer = 0
        max_len = 0
        for i, char in enumerate(s):
            if char in dic:
                pointer = max(pointer, dic[char] + 1)
            max_len = max(i - pointer + 1, max_len)
            dic[char] = i
        return max_len

S = Solution()
print(S.lengthOfLongestSubstring('pwpkewep'))
