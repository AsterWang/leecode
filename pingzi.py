import sys
res = []
n = sys.stdin.readline().strip()
n = int(n)
while True:
    x = sys.stdin.readline().strip()
    if x == '':
        break
    x = int(x)
    if x not in res:
        res.append(x)
res.sort()
for num in res:
    print(num)
