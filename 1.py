import sys
from queue import Queue
def get_sum(row, column):
    s = 0
    while row:
        s += row % 10
        row /= 10
    while column:
        s += column % 10
        column /= 10
    return s

def dfs(row, column, thres):
    if row < 0 or column < 0:
        return 0
    q = Queue()
    dp = [[False] * row for _ in range(column)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    res = 0
    q.put((0,0))
    while not q.empty():
        t = q.get()
        if dp[t[0]][t[1]] or get_sum(t[0], t[1]) > thres:
            continue
        res += 1
        dp[t[0]][t[1]] = True
        for i in range(4):
            x = t[0] + dx[i]
            y = t[1] + dy[i]
            if (x >= 0 and x < row and y >= 0 and y < column):
                q.put((x,y))
    return res



while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    num = line.split(' ')
    nums = [int(x) for x in num]
    m,n,k = nums[0],nums[1],nums[2]
    res = dfs(m,n,k)
    print(res)
