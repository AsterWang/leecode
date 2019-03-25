'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Note:
    1.One house can be robbed or not robbed
    2.Consider the circle condition, we could either start from 1st or 2rd house to rob, then calculate the maximum money
    the robber could get in these two conditions respectively.
    3.Regarding to first condition, it's obvious that if we rob the first house, we could not rob the last house.

                1   2   5   2   1   3
    r_ff        1   2   6   4   7   9  (we need to remove the last element because of mutual exclusion of robbing first house and robbing last house)
    no_r_ff     0   1   2   6   6   7
    r_fs        0   2   5   4   6   8
    no_r_fs     0   0   2   5   5   6
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        rb_ff = [nums[0]]
        no_rb_ff = [0]
        rb_fs, no_rb_fs = [0], [0]
        for n in nums[1:]:
            tmp1 = rb_ff[-1]
            rb_ff.append(no_rb_ff[-1] + n)
            no_rb_ff.append(max(no_rb_ff[-1], tmp1))

            tmp2 = rb_fs[-1]
            rb_fs.append(no_rb_fs[-1] + n)
            no_rb_fs.append(max(no_rb_fs[-1], tmp2))
        return max(rb_ff[-2], no_rb_ff[-1], rb_fs[-1], no_rb_fs[-1])
