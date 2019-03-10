import sys
offset, n, l1, l2 = sys.stdin.readline().strip().split(' ')
offset = int(offset)
n = int(n)
l1 = int(l1)
l2 = int(l2)
if offset <= l1:
    if offset + n <= l1:
        start1, end1, start2, end2 = offset, offset + n, 0 ,0
    elif offset + n > l1 and offset + n <= l1 + l2:
        start1, end1, start2, end2 = offset, l1, 0, offset + n - l1
    else:
        start1, end1, start2, end2 = offset, l1, 0, l2
else:
    start1, end1, start2, end2 = l1, l1, offset - l1, offset + n - l1
print(' '.join([str(start1), str(end1), str(start2), str(end2)]))