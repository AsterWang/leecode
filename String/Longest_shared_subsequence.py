class Solution(object):
    def lengthOfSharedLongestSuseq(self, arr1, arr2):
    	if not arr1 or not arr2:
    		return 0
    	dp = [[0] * (len(arr2) + 1) for _ in range(len(arr1) + 1)]
    	for i in range(1, len(arr1) + 1):
    		for j in range(1, len(arr2) + 1):
    			if arr1[i - 1] == arr2[j - 1]:
    				dp[i][j] = dp[i - 1][j - 1] + 1
    			else:
    				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    	print(dp[-1][-1])

    def lengthOfSharedLongestSubstring(self, arr1, arr2):
    	if not arr1 or not arr2:
    		return 0
    	dp = [[0] * (len(arr2) + 1) for _ in range(len(arr1) + 1)]
    	mx_len = 0
    	for i in range(1, len(arr1) + 1):
    		for j in range(1, len(arr2) + 1):
    			if arr1[i - 1] == arr2[j - 1]:
    				dp[i][j] = dp[i - 1][j - 1] + 1
    				mx_len = max(mx_len, dp[i][j])
    	print(mx_len)



s = Solution()
s.lengthOfSharedLongestSuseq('ABCBDAB', 'BDCABA')
s.lengthOfSharedLongestSubstring('AABBSCSDSA', 'ABBSFAFS')