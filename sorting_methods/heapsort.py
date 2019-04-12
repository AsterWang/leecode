#create a maximum heap
def adjust_heap(arr, i, length):
	tmp = arr[i]
	k = 2 * i + 1
	while k < length:
		#maximum heap
		if k + 1 < length and arr[k + 1] > arr[k]:
			k += 1
		if arr[k] > tmp:
			arr[i] = arr[k]
			i = k
			k = 2 * i + 1
		else:
			break
	arr[i] = tmp

#create a minimum heap
def adjust_heap_to_minheap(arr, i, length):
	tmp = arr[i]
	k = i * 2 + 1
	while k < length:
		if k + 1 < length and arr[k + 1] < arr[k]:
			k += 1
		if arr[k] < tmp:
			arr[i] = arr[k]
			i = k
			k = i * 2 +1
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
	#sorting
	for j in range(length - 1, 0, -1):
		swap(arr, j, 0)
		adjust_heap(arr, 0, j)

def set_top(arr, top):
	arr[0] = top
	adjust_heap(arr, 0, len(arr))

def heap_find_topK(arr, k):
	top = [i for i in arr[:k]]
	heap_sort(top)
	for i in range(k, len(arr)):
		tmp = top[0]
		if arr[i] > tmp:
			set_top(top, arr[i])
	return top

L = [50,16,30,10,60,90,2,80]
heap_sort(L)
topK = heap_find_topK(L, 4)
print(topK)


