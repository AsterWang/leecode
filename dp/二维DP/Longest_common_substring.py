def longest_common_substring(arr1, arr2):
    length1 = len(arr1)
    length2 = len(arr2)

    dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]
    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            if arr1[i - 1] != arr2[j - 1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = dp[i-1][j-1] + 1
    print(dp[-1][-1])


# def shortest_common_super_sequence(arr1, arr2):
#     length1 = len(arr1)
#     length2 = len(arr2)

#     dp = [[[] for _ in range(length2 + 1)]for _ in range(length1 + 1)]
#     # print(dp)
#     for i in range(1, length1 + 1):
#         for j in range(1, length2 + 1):
#             if arr1[i - 1] != arr2[j - 1]:
#                 if len(dp[i-1][j]) > len(dp[i][j-1]):
#                     dp[i][j] = dp[i-1][j] 
#                 else:
#                     dp[i][j] = dp[i][j-1]
#             else:
#                 dp[i][j] = dp[i-1][j-1] + [arr1[i-1]]
#     print(dp[-1][-1])

longest_common_substring("abcdbcd", "efbcdbc")
# shortest_common_super_sequence("abcdbcd", "efbcdbc")
