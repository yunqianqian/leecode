def solution(s):
    if len(s) % 2 == 1:
        return False
    dicts = {")":"(","}":"{","]":"["}
    stack = []
    for itemx in s:
        if itemx in dicts.values():
            stack.append(itemx)
        else:
            if not stack or stack[-1] != dicts[itemx]:
                return False
            stack.pop()
    return len(stack) == 0
            




if __name__ == "__main__":

    strs = {
    "((":True,
    "{}{}":True,
    "[{}][{}]":True,
    "(]":False,
    "{":False,
    "{([])}":True,
    "{}[(}]":False,
    "{[[{}(]])}":False
    }
    for s in strs:
        print(solution(s))