'''
backtracking to solve 0/1 backpack to get maximum weight
'''
class Solution:
    def __init__(self):
        self.max_weight = -float('inf')
    def find_max_weight(self, i, cur_weight, items, w):
        if cur_weight == w or i == len(items):
            if cur_weight > self.max_weight:
                self.max_weight = cur_weight
            return
        self.find_max_weight(i + 1, cur_weight, items, w)
        if cur_weight + items[i] <= w:
            self.find_max_weight(i + 1, cur_weight + items[i], items, w)
        return self.max_weight

s = Solution()
res = s.find_max_weight(0,0,[7,30, 33, 10, 30, 50, 60],100)
print(res)