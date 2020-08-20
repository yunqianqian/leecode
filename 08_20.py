'''66.加一'''
def plusOne(digits):
	strs = ""
	res = []
	if len(digits) == 0:
		return [1]
	for item in digits:
		strs += str(item)
	strs = int(strs) + 1
	for item in str(strs):
		res.append(int(item))
	return res



print(plusOne([]))