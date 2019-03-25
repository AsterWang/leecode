def binary_search(arr, key):
	start = 0
	end = len(arr) - 1
	while start <= end:
		mid = (end + start) // 2
		if arr[mid] < key:
			start = mid + 1
		elif arr[mid] > key:
			end = mid -1
		else:
			return mid
	return -1

def binSearch_rec(arr, start, end, key):
	mid = (end + start) // 2
	if arr[mid] == key:
		return mid
	if start >= end:
		return -1

	if arr[mid] < key:
		return binSearch_rec(arr, mid + 1, end, key)
	elif arr[mid] > key:
		return binSearch_rec(arr,start, mid - 1, key)


arr = [1,2,4,6,11,222,1321]
print(binary_search(arr, 222))
print(binSearch_rec(arr, 0, len(arr) - 1, 22222))