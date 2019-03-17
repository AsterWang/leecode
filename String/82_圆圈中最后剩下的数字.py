class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        res = [i for i in range(n)]
        i = -1
        length = len(res)
        while length > 1:
            i = (i + m) % length
            res.pop(i)
            i -= 1
            length -= 1
        return res[-1]
