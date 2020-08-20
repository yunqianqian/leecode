'''58.最后一个单词的长度'''
def soulution(strs):
	if not strs:
		return 0
	s = strs.strip().split()
	if not s:
		return 0
	else:
		return len(s[-1])


strs = "Hello world!"
strs = " "
res = 0
strs = "a "
res = 1
print(soulution(strs))



