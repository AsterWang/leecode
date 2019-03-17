'''
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。

2～10为数字本身，A为1，J为11，Q为12，K为13，大小王可以看做任意数字。

为了方便，大小王均以0来表示，并且假设这副牌中大小王均有两张。

样例1
输入：[8,9,10,11,12]

输出：true
样例2
输入：[0,8,9,11,12]

输出：true

思路：
    先对手中的牌排序

    1.手中的牌不能有对子
    2.前后两张牌的差值 - 1 < 手中大小王的个数
'''
class Solution(object):
    def isContinuous(self, numbers):
        """
        :type numbers: List[int]
        :rtype: bool
        """
        if not numbers:
            return False
        numbers.sort()
        zero_num = 0
        for i, n in enumerate(numbers[:-1]):
            if n == 0:
                zero_num +=1
            else:
                #有对子
                if numbers[i+1] == n:
                    return False
                if numbers[i+1] - n == 1:
                    continue
                if numbers[i+1] - n - 1 > zero_num:
                    return False
                zero_num -= numbers[i+1] - n - 1
        return True
