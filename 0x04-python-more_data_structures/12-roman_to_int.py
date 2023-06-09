#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None) or (isinstance(roman_string, str) is False):
        return 0
    dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
    res = 0
    for i in range(len(roman_string)):
        j = dic[roman_string[i]]
        if i + 1 < len(roman_string) and j < dic[roman_string[i + 1]]:
            res -= dic[roman_string[i]]
        else:
            res += dic[roman_string[i]]
    return res
