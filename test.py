def is_valid(res, index):
    if not res[index].isdigit():
        return False

    if res[index-1].isdigit() or res[index+1].isdigit():
        return False

    return True

def replace_all(string):
    temp = list(string)
    n = len(temp)
    for i in range(n):
        if is_valid(string, i):
            if temp[i] == "3":
                temp[i] = "e"
            if temp[i] == "0":
                temp[i] = "o"
        if temp[i] == "@":
            temp[i] = "a"

    return ''.join(temp)

st1="Profile will be y3arly Recurring. Profile video length should be m@x 5 min only. 190, 100, 80 ,80 Platform will accessible after login only.No Instant Chat only message B0ard Functionality."
r = replace_all(st1)
print(r)