'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

init state : dp[0] = True so that if substring of s, eg.s[0:5] = 'leet' in dicitonary, we could set dp[5] = True
func: if we found a matched substring ,we need to confirm that substring s[:i - len(word)] also satisfies.
        so dp[i] = True if s[i - len(word) : i] == word and dp[i - len(word)]
result
    return dp[-1]
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True
        for i in range(1, length + 1):
            for word in wordDict:
                if i >= len(word):
                    if s[i-len(word):i] == word and dp[i -len(word)]:
                        dp[i] = True
                        break
        return dp[-1]
        