class Solution(object):
    def add(num1, num2):
        L1 = list(num1)
        L2 = list(num2)
        remain = 0
        result = []
        while L1 or L2:
            n1 = ord(L1.pop()) - ord('0') if len(L1) > 0 else 0
            n2 = ord(L2.pop()) - ord('0') if len(L2) > 0 else 0
            tmp = n1 + n2 + remain
            x = tmp % 10
            result.append(x)
            remain = tmp // 10
        if remain > 0:
            result.append(remain)
        return ''.join(str(x) for x in result[::-1])