def longestCommonPerfix(strs):
    num = len(strs[0])
    logest = 0
    # for sqe, item in enumerate(strs):
    #     if len(item) > num:
    #         num = len(item)
    #         logest = item
    # print (num,logest)
    for item in range(len(strs)):
        if len(strs[item]) < num:
            num = len(strs[item])
            logest = item
    print(num, logest)
    strx = strs[logest]
    print (strx)
    for item in range(len(strx)):
        s = set()
        print("item:",strx[item])
        for x in strs:
            for y in range(len(x)):
                if strx[item] != x[y]:
                    s.add(False)
                else:
                    print("1")
                    s.add(True)
        print(s)
        if s == {True}:
            return strx[:item + 1]
    return None


def demo1(strs):
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    num = len(strs[0])
    logest = 0
    for item in range(len(strs)):
        if len(strs[item]) < num:
            num = len(strs[item])
            logest = item
    strx = strs[logest]
    if len(strx) == 0:
        return ""
    for itemx in range(len(strx)):
        print(itemx)
        for itemy in strs[0:]:
            if strx[itemx] != itemy[itemx]:
                print(itemx)
                if itemx == 0:
                    return ""
                return (strx)[0:itemx]
    
    return (strx)[0:itemx+1]




if __name__ =="__main__":
    print ("res:",demo1( ["ca","a"]))