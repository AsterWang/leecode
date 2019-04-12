'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

假设数组非空，并且一定存在满足条件的数字。

思考题：

假设要求只能使用 O(n) 的时间和额外 O(1) 的空间，该怎么做呢？
样例
输入：[1,2,1,1,3]

输出：1

思路：
    维护两个值：一个是当前数字出现的次数，一个是candidate
    如果当前数字跟candidate不同，则将time - 1,如果time == 0，则更改candidate为当前数字，并将
    times设为1。原因是因为一个数字出现的次数超过一半，那么到最后times所对应的candidate一定是这个众数。
'''
class Solution(object):
    def moreThanHalfNum_Solution(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = 1
        res = nums[0]
        for i in range(1, len(nums)):
            # print(times)
            if nums[i] != res:
                times -=1
                if times == 0:
                    times = 1
                    res = nums[i]
            else:
                times += 1
        return res
        
        