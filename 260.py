import sys
from collections import defaultdict
while True:
	line = sys.stdin.readline().strip()
	if not line:
		break
	hash_key = int(line.split('/')[0])
	key_str = line.split('/')[1]
	tmp = key_str.split(',')
	gap = set()
	res = defaultdict(list)

	for str_tmp in tmp:
		if str_tmp.find('-') > 0:
			begin, end = str_tmp.split('-')
			for i in range(int(begin), int(end) + 1):
				gap.add(i)
		else:
			gap.add(int(str_tmp))
	# print('gap is', gap)

	for num in gap:
		key = num % hash_key
		res[key].append(num)

	res_key, res_val = "", []
	min_len = -float('inf')
	for key, val in res.items():
		if len(val) > min_len:
			res_key = key
			res_val = val
			min_len = len(val)
	res_val.sort(reverse=True)
	val_str = ' '.join([str(x) for x in res_val])
	res_str = '{0}-{1}-{2}'.format(len(res_val), res_key, val_str)
	# print(res)
	print(res_str)

