class Solution(object):
    def findContinuousSequence(self, sum):
        """
        :type sum: int
        :rtype: List[List[int]]
        """
        end = (sum + 1) // 2
        start = 1
        t = 0
        res = []
        tmp = []
        while start < end:
            if t > sum :
                t -= tmp.pop(0)
            else:
                t += start
                tmp.append(start)
                if t == sum:
                    res.append(tmp[::])
                start += 1
                t += start
                tmp.append(start)
        return res

s = Solution()
res =s.findContinuousSequence(15)
print(res)
