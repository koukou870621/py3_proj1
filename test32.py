#!/usr/bin/python3

def deleteCharacters(str, charSet):
    hash = [0]*256
    currentIndex = 0
    if not charSet:
        return str
    for i in range(0, len(charSet)):
        hash[ord(charSet[i])] = 1
    str_list = list(str)
    for i in range(0, len(str)):
        if not hash[ord(str[i])]:
            str_list[currentIndex] = str_list[i]
            currentIndex += 1
    str_list[currentIndex] = '\0'
    zero_index = str_list.index('\0')
    filter_array = str_list[:zero_index]
    return ''.join(filter_array)


def test32():
    s = "a"
    s2 = "aca"
    print(deleteCharacters(s2, s))


test32()
