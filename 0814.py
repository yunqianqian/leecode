def isPalindrome(x):
    for item in range(0, len(str(x))):
        if str(x)[item] == str(x)[len(str(x)) - 1- item]:
            continue
        else:
            return False
    return True


print(isPalindrome(1))