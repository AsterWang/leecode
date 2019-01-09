'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。

假设压入栈的所有数字均不相等。

例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。

注意：若两个序列为空或长度不等则视为并不是一个栈的压入、弹出序列。

样例
输入：[1,2,3,4,5]
      [4,5,3,2,1]

输出：true

算法：
    1.  用一个stack 来模拟出栈和入栈的操作
    2.  每次push一个数，就检查有没有可能pop出来。如果可以pop，那就移动到popV的下一个数来检查
    3.  push完成后，检查stack中是否为空，如果是空，说明popV中的顺序是合法的（只有合法才会出现空的stack）
'''

class Solution(object):
    def isPopOrder(self, pushV, popV):
        """
        :type pushV: list[int]
        :type popV: list[int]
        :rtype: bool
        """
        if not pushV and not popV:
            return False
        length = len(pushV)
        if length != len(popV):return False
        tmp = []
        pop_num = 0
        for push_num in range(length):
            tmp.append(pushV[push_num])
            while len(tmp) != 0 and tmp[-1] == popV[pop_num]:
                tmp.pop()
                pop_num += 1
        if len(tmp) == 0:return True
        return False