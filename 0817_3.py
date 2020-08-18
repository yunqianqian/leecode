def removeEle(nums, val):
    i = 0
    for item in range(len(nums)):
        if nums[item] != val:
            nums[i] = nums[item]
            i += 1
    print(nums)
    return i
print(removeEle(nums = [], val = 2))

