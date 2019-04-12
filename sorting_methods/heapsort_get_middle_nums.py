'''
堆的应用三:利用堆求中位数.

我们需要维护两个堆，一个大顶堆，一个小顶堆。大顶堆中存储前半部分数据，小顶堆中存储后半部分数据，
且小顶堆中的数 据都大于大顶堆中的数据。
也就是说，如果有n个数据，n是偶数，我们从小到大排序，那前2/n个数据存储在大顶堆中，
后 2/n 个数据 存储在小顶堆中。这样，大顶堆中的堆顶元素就是我们要找的中位数。
如果n是奇数，情况是类似的，大顶堆就存储 2/n + 1 个数据，小顶堆中就存储 2/n 个数据

'''

import sys
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

def find_middle_num(arr):
	heap_sort(arr)
	print(arr)
	left = [x for x in arr[:len(arr) // 2]]
	right = [x for x in arr[len(arr) // 2:]]
	#adjust left to maximum heap
	mid = len(left) // 2 - 1
	length = len(left)
	for i in range(mid, -1 , -1):
		adjust_heap(left, i, length)
	print(left)
	print(right)
	return left, right

def heap_up_with_maxheap(arr, index):
	if index > 0:
		parent = index // 2
		parent_val = arr[parent]
		index_val = arr[index]
		if parent_val < index_val:
			arr[parent], arr[index] = arr[index], arr[parent]
			heap_up_with_maxheap(arr, parent)

def heap_up_with_minheap(arr, index):
	if index > 0:
		parent = index // 2
		parent_val = arr[parent]
		index_val = arr[index]
		if parent_val > index_val:
			arr[parent], arr[index] = arr[index], arr[parent]
			heap_up_with_minheap(arr, parent)

def insert_minheap(arr, num):
	if len(arr) == 0:
		arr.append(num)
	else:
		arr.append(num)
		heap_up_with_minheap(arr, len(arr) - 1)

def insert_maxheap(arr, num):
	if len(arr) == 0:
		arr.append(num)
	else:
		arr.append(num)
		heap_up_with_maxheap(arr, len(arr) - 1)

L = [50,16,30,10,60,90,2,80]
left, right = find_middle_num(L)
while True:
	num = sys.stdin.readline().strip()
	if not num:
		break
	num = int(num)

    # Left part is maximum heap
	if num <= left[0]:
		insert_maxheap(left, num)
		swap(left, 0, len(left) - 1)
		adjust_heap(left, 0, len(left) - 1)
		tmp = left.pop()
		insert_minheap(right,tmp)
    # Right part is minimum heap
	elif num >= right[0]:
		insert_minheap(right, num)
		swap(right, 0, len(right) - 1)
		adjust_heap_to_minheap(right, 0, len(right) - 1)
		tmp = right.pop()
		insert_maxheap(left, tmp)
	
	print(left)
	print(right)
	print("==========================================")
