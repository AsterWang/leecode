'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

思路：
    本题强调的一个概念是分组：确定一位数后，以这一位数开始的组内有多少元素。例如 nums = [1,2,3],那么确定第一位是1，那么len(startWith(1)) = 2。
    确定 kth 所在的分组后，在对确定的这个组进行更细致的划分。例如：确定第一个元素是2后，我们对starWith(2) = [213, 231]进行划分，现在我们需要
    确定的是 kth 在该子集内的哪个小组内。。。以此类推，直到所有的数都被遍历。
'''
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = []
        fac = [0 for _ in range(n)]
        fac[0] = 1
        for i in range(1, n):
            fac[i] = fac[i - 1] * i
        nums = [x for x in range(1, n + 1)]
        k -=1
        for i in range(n):
            num = nums.pop(k / fac[n - 1 - i])
            result.append(str(num))
            k = k % fac[n - 1 - i]
        return ''.join(result)
            
        