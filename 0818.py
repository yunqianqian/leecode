'''实现strStr()'''
def solution(haystack, needle):
    if len(haystack) < len(needle):
        return -1
    if (len(needle) == 0):
        return 0
    for itemx in range(len(haystack)):
        if len(haystack) - itemx < len(needle):
            return -1
        if haystack[itemx] == needle[0]:
            for itemz in range(len(needle)):
                if haystack[itemx + itemz] == needle[itemz]:
                    if itemz == len(needle) -1:
                        return itemx
                else:
                    break

    return -1

print(solution(haystack = "mississippi", needle = "issip"))
