'''搜索插入位置 '''

def searchInsert(nums, target):
	i = 0
	for item in range(len(nums)):
		if nums[item] == target:
			return item
		if (nums[item] < target):
			if item == len(nums) - 1:
				return len(nums)
			else:
				if nums[item + 1] >= target:
					i = item+1
	return i

if __name__ == "__main__":
	print(searchInsert([], 0))
