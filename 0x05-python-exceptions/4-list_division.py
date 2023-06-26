#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = None
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            new_list.append(div)
        except TypeError:
            print("wrong type")
            div = 0
            new_list.append(div)
        except IndexError:
            print("out of range")
            div = 0
            new_list.append(div)
        except ZeroDivisionError:
            print("division by 0")
            div = 0
            new_list.append(div)
        finally:
            pass
    return new_list
