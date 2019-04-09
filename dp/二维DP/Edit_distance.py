'''
    Edit Distance Given two text strings A of length n and B of length m, you
    want to transform A into B. You are allowed to insert a character, delete a
    character and to replace a character with another one. An insertion costs ci, a
    deletion costs cd and a replacement costs cr.
'''
def edit_distance(arr1, arr2, ci, cd, cr):
    len1 = len(arr1)
    len2 = len(arr2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    for i in range(len1 + 1):
        dp[i][0] = i * ci
    for j in range(len2 + 1):
        dp[0][j] = j * ci
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if arr1[i - 1] == arr2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1] + ci, dp[i - 1][j] + cd, dp[i - 1][j - 1] + cr)
    return dp[-1][-1]
res = edit_distance("ABCEB", "AFCB", 1, 2, 3)
print(res)