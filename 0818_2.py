'''实现strStr()'''
def solution(haystack, needle):
    if len(haystack) < len(needle):
        return -1
    if len(needle) == 0:
        return 0
    Len = len(needle)
    for itemx in range(len(haystack)):
        if len(haystack) - itemx < len(needle):
            return -1
        print(itemx)
        print(haystack[itemx:itemx+Len])
        if haystack[itemx:itemx+Len] == needle:
            return itemx
    return -1

print(solution(haystack = "mississippi", needle = "issip"))
