def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		left = arr[:mid]
		right = arr[mid:]
		merge_sort(left)
		merge_sort(right)

		i, j, index = 0, 0, 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[index] = left[i]
				i += 1
			else:
				arr[index] = right[j]
				j += 1
			index += 1
		while i < len(left):
			arr[index] = left[i]
			i += 1
			index += 1
		while j < len(right):
			arr[index] = right[j]
			j += 1
			index += 1

arr = [54,26,93,17,77,31,44,55,20]
merge_sort(arr)
print(arr)
