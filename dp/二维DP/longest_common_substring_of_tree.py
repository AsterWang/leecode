def longest_substring_of_three(s1, s2, s3):
    l1, l2, l3 = len(s1), len(s2), len(s3)
    dp = [[[0] * (l3 + 1) for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            for n in range(1, l3 + 1):
                if s1[i - 1] == s2[j - 1] and s1[i - 1] == s3[n - 1]:
                    dp[i][j][n] = dp[i-1][j-1][n-1] + 1
                else:
                    dp[i][j][n] = max(dp[i][j-1][n], dp[i][j][n-1], dp[i-1][j][n])
    return dp[-1][-1][-1]

result = longest_substring_of_three("abcdsdf", "aadbcdfeqeqfds", "e132bcdf..")
print(result)