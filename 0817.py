'''26. 删除排序数组中的重复项'''
def removeDup(nums):
    i,j = 0,1
    for j in range(len(nums)):
        if nums[i] == nums[j]:
           j += 1
        else:
            i += 1
            nums[i] = nums[j]
    print(nums)
    return i+1

if __name__ =='__main__':
    print(removeDup([1]))  
    print(removeDup([1,1,2]))  
    print(removeDup([0,0,1,1,1,2,2,3,3,4]))  

