'''
思路	：
	与快排相比，两者唯一的不同是在对”分治”结果的使用上。我们知道，分治函数会返回一个position，
	在position左边的数都比第position个数小，在position右边的数都比第position大。我们不妨不断调用分治函数，
	直到它输出的position = K-1，此时position前面的K个数（0到K-1）就是要找的前K个数。

时间复杂度:O(N)
'''
#from largest to smallest
def partition(arr, low, high):
	i = low - 1
	pivot = arr[high]
	for j in range(low, high):
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1

def partition(arr, low, high):
	i = low - 1
	pivot = arr[high]
	for j in range(low, high):
		if arr[j] > pivot:
			i += 1
			arr[j], arr[i] = arr[j], arr[i]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1
#from smallest to largest
# def partition(arr, low, high):
# 	i = low - 1
# 	pivot = arr[high]
# 	for j in range(low, high):
# 		if arr[i] < pivot:
# 			i += 1
# 			arr[i], arr[j] = arr[j], arr[i]
# 	arr[i + 1], arr[high] = arr[high], arr[i + 1]
# 	return i + 1

def getTopK(arr, k):
	low = 0
	high = len(arr) - 1
	pi = partition(arr, low, high)
	while pi != k - 1:
		if pi > k - 1:
			print("pi > k - 1")
			high = pi - 1
			pi = partition(arr, low, high)

		if pi < k - 1:
			print("pi < k - 1")
			low = pi + 1
			pi = partition(arr, low, high)

arr = [9, 3, 1, 10, 5, 7, 6, 2, 8, 0]
getTopK(arr, 3)
for i in arr:
	print(i, ",")