# def adjust_heap(arr, i, length):
# 	k = i * 2 + 1
# 	tmp = arr[i]
# 	while k < length:
# 		if k + 1 < length and arr[k + 1] > arr[k]:
# 			k += 1
# 		if tmp < arr[k]:
# 			arr[i] = arr[k]
# 			i = k
# 			k = 2 * k + 1
# 		else:
# 			break
# 	arr[i] = tmp

# def swap(arr, i, j):
# 	arr[i], arr[j] = arr[j], arr[i]

# def sort(arr):
# 	length = len(arr)
# 	start = length / 2 - 1
# 	#create maximum heap
# 	for i in range(start, -1, -1):
# 		adjust_heap(arr, i, length)

# 	#sortring
# 	for j in range(length-1, 0, -1):
# 		swap(arr, 0, j)
# 		adjust_heap(arr, 0, j)
def adjust_heap(arr, i, length):
	tmp = arr[i]
	k = 2 * i + 1
	while k < length:
		if k + 1 < length and arr[k + 1] > arr[k]:
			k += 1
		if arr[k] > tmp:
			arr[i] = arr[k]
			i = k
			k = 2 * i + 1
		else:
			break
	arr[i] = tmp

def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]

def heap_sort(arr):
	#creating maximum headp
	mid = len(arr) // 2 - 1
	length = len(arr)
	for i in range(mid, -1 , -1):
		adjust_heap(arr, i, length)
	print(arr)
	#sorting
	for j in range(length - 1, 0, -1):
		swap(arr, j, 0)
		adjust_heap(arr, 0, j)



L = [50,16,30,10,60,90,2,80]
heap_sort(L)
print(L)		