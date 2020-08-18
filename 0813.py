"""
我的想法很简单，先获取中间的位置，比较，相同则退出;返回True,
大于则获取大的部分，然后比较，小则获取小的部分比较。最后返回结果。
可能是受惯性思维吧，为啥每次都把List的部分，重新赋值给新的List呢？其实可以直接对List的标号进行二进制排列。
我的思维太简单了，直接对数据切割，对数组中元素进行二分，难道不是对数组中的标号进行切分？

重点：  二分法可以对列表的标号进行二分。

"""


def binary_search_1(List, item):
    num = len(List)
    if item > List[-1] or item < List[0]:
        return False
    if item == List[int(num/2)]:
        return True
    elif item > List[int(num/2)]:
        List = List[int(num/2)+1: num]
        return binary_search_1(List, item)
    else:
        List = List[0:int(num/2)]
        return binary_search_1(List, item)

"""
列表俩说，通过标号可以很快找到对应的值，二分法应该是对标号的二分，这样还方便找到对应目标值的标号
"""


def binary_search_2(List, item, first_num, end_num):
    if item > List[-1] or item < List[0]:
        return False
    middle_num = int((first_num + end_num)/2)
    if item > List[middle_num]:
        return binary_search_2(List, item, middle_num+1, end_num)
    elif item < List[middle_num]:
        return binary_search_2(List, item, first_num, middle_num)
    else:
        print(middle_num)
        return True


if __name__ == "__main__":
    List =[]
    for item in range(1,1025):
        List.append(item)
    print(List)
    print(binary_search_1(List, 10))
    print(binary_search_2(List, 1023, 0, len(List)))