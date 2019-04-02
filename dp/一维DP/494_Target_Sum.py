'''
Rather than use a variable or list to keep track of the state in DP,
we use a dictionary to store all statistics we currently have since the same sums
are recorded together as keys in dictionary.
'''
from collections import defaultdict
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        d = defaultdict(int)
        if nums[0] != 0:
            d[-nums[0]] = 1
            d[nums[0]] = 1
        else:
            d[nums[0]] = 2
        for i, n in enumerate(nums[1:], 1):
            tmp = defaultdict(int)
            for k, v in d.items():
                tmp[k + n] = tmp[k + n] + v
                tmp[k - n] = tmp[k - n] + v
            d = tmp
        return d[S]