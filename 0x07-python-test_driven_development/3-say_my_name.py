#!/usr/bin/python3
"""
this is "3-say_my_name"
functions:
    def say_my_name(first_name, last_name=""):    
"""
def say_my_name(first_name, last_name=""):
    """
    function that print names

    Args:
        first_name (str): first name
        last_name (str): last name. Defaults to "".

    Raises:
        TypeError: must be string
    """
    if type(first_name) != str or type(last_name) != str:
        if type(first_name) != str:
            raise TypeError("first_name must be a string")
        elif type(last_name) != str:
            raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))

