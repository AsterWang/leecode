class Solution(object):
	"""docstring for Solution"""
	def sum(self, arr, val):
		arr.sort()
		i = 0
		j = len(arr) - 1
		while (i < j):
			if arr[i] + arr[j] == val:
				return True
			elif arr[i] + arr[j] > val:
				j -=1
			else:
				i +=1
		return False


arr = [1,2,31,23,1,4,1,24,5,6,2,2]
s = Solution()
res = s.sum(arr, 100)
print(res)