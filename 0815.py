Str="MCMXCIV"

Dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
value = 0
for item in range(len(Str)-1):
    if Dict[Str[item]] >= Dict[Str[item + 1]]:
        value += Dict[Str[item]]
    else:
        value -= Dict[Str[item]]
value += Dict[Str[len(Str) - 1]]
print(value)