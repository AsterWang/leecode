import sys
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    nums1, nums2 = line.split(' ')
    nums1 = nums1[::-1]
    nums2 = nums2[::-1]
    length1 = len(nums1)
    length2 = len(nums2)
    num = [0 for _ in range(length1 + length2)]
    result = []
    remain = 0
    for i in range(length1):
        for j in range(length2):
            num[i + j] += int(nums1[i]) * int(nums2[j])
    for i in range(length1 + length2):
        x = (num[i] + remain)
        y = x % 10
        remain = x // 10
        result.append(y)
    for i in range(length1 + length2 - 1, -1):
        if result[i] != 0:
            result = result[i:]
    print(''.join(str(x) for x in result[::-1]))