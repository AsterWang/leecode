import sys
n = int(sys.stdin.readline().strip())
while True:
    nums = []
    for _ in range(n):
        x = sys.stdin.readline().strip().split(' ')
        nums.append((int(x[0]), int(x[1])))
    nums.sort(reverse = True, key= lambda x : x[0])

    y_max = nums[0][1]
    res = [nums[0]]
    print(nums)
    for num in nums[1:]:
        if num[1] > y_max:
            res.append(num)
            y_max = num[1]
    res.sort(reverse=False,key = lambda x : x[0])
    for num in res:
        print(str(num[0]) + " " + str(num[1]))
