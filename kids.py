import sys
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    n = int(line)
    h = [int(x) for x in sys.stdin.readline().strip().split()]
    m = int(sys.stdin.readline().strip())
    w = [int(x) for x in sys.stdin.readline().strip().split()]

    h.sort(reverse = True)
    w.sort(reverse = True)
    j = 0
    result = 0
    for x in w:
        while j < n and x < h[j]:
            j += 1
        if j < n:
            result += 1
            j += 1
    print(result)