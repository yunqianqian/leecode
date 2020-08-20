'''67.二进制求和'''
def addBinary(a,b):
	flag = 0
	res = ""
	if len(a) >= len(b):
		Max = a
		Len = len(b)
	Max = b
	Len = len(a)
	for item in range(Len-1,-1,-1):
		if int(a[item]) + int(b[item]) + flag == 3:
			flag = 1
			res += "1"
		if int(a[item]) + int(b[item]) + flag == 2:
			flag = 1
			res += "0"
		else:
			flag = 0
			res += "0"
	return 

