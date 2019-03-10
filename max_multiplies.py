import sys
while True:
    line = sys.stdin.readline().strip()
    nums = line.split(' ')
    if line == '':
        break
    if len(nums) < 3:
        print(0)
    else:
        max1 = max2 = max3 = -float('inf')
        min1 = min2 = min3 = float('inf')
        for num in nums:
            num = int(num)
            if num >= max1:
                max1, max2, max3 = num, max1, max2
            elif num >= max2:
                max2, max3 = num, max3
            elif num >= max3:
                max3 = num

            if num <= min1:
                min1, min2, min3 = num, min1, min3
            elif num <= min2:
                min2, min3 = num, min2
            elif num <= min3:
                min3 = num
        print(max(max1 * max2 * max3, min1 * min2 * max1))