class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.dfs(s, [],result)
        return result

    def dfs(self, s, path, result):
        if not s:
            result.append(path[:])
            return

        for i in range(1, len(s) + 1):
            if self.is_palin(s[:i]):
                path.append(s[:i])
                self.dfs(s[i:], path, result)
                path.pop()
    def is_palin(self, s):
        return s == s[::-1]

s = Solution()
print(s.partition('aabc'))
