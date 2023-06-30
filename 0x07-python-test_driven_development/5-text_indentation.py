#!/usr/bin/python3
"""
this is "5-text_indentation"
functions:
    def text_indentation(text):
"""


def text_indentation(text):
    """
    function that print text but if there is . or ? or : print new line

    Raises:
        TypeError: text must be a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        check = 0
        for i in text:
            if i == "." or i == "?" or i == ":":
                print("{}".format(i), end='')
                print("\n")
                check = 1
            else:
                if check == 0:
                    print("{}".format(i), end='')
                check = 0
