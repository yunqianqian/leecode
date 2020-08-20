'''38.外观数列'''

def countAndSay(n):
	if n == 1:
		return "1"
	value = countAndSay(n-1)
	strs = ""
	num = 1
	for item in range(len(value)):
		if item == len(value) - 1:
			strs += str(num)+value[item]
			return strs
		if value[item] != value[item + 1]:
			strs += str(num)+value[item]
			num = 1
		else:
			num += 1

# print(countAndSay(10))

#补充
'''
0、1、1、2、3、5、8、13、21、34、……在数学上，
斐波那契数列以如下被以递推的方法定义：
F(0) = 0
F(1)=1，F(2)=1, 
F(n)=F(n - 1) + F(n - 2)
'''

def Fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return Fib(n-1) + Fib(n-2)


print(Fib(10))
