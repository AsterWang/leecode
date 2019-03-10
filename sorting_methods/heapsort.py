def adjust_heap(arr, i, length):
	k = i * 2 + 1
	tmp = arr[i]
	while k < length:
		if k + 1 < length and arr[k + 1] > arr[k]:
			k += 1
		if tmp < arr[k]:
			arr[i] = arr[k]
			i = k
			k = 2 * k + 1
		else:
			break
	arr[i] = tmp

def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]

def sort(arr):
	length = len(arr)
	start = length / 2 - 1
	#create maximum heap
	for i in range(start, -1, -1):
		adjust_heap(arr, i, length)

	#sortring
	for j in range(length-1, 0, -1):
		swap(arr, 0, j)
		adjust_heap(arr, 0, j)


L = [50,16,30,10,60,90,2,80]
sort(L)
print(L)		