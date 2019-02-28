def find(arr, vmid):
	count = 0
	for i in arr:
		if i >= vmid:
			count += 1
	return count

def find_Nth_largest_number(arr, K):
	delta = 0.000000001
	vmax = max(arr)
	vmin = min(arr)

	while vmax - vmin > delta:
		vmid = vmin + (vmax - vmin) * 0.5
		if find(arr, vmid) >= K:
			vmin = vmid
		else:
			vmax = vmid
	print(vmid)


find_Nth_largest_number([10,90, 70, 60, 5, 4, 15], 6)


