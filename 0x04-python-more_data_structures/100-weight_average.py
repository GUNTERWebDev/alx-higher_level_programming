#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        numerator = 0
        denominator = 0
        for i in range(len(my_list)):
            numerator += my_list[i][0] * my_list[i][1]
            denominator += my_list[i][1]
        return numerator / denominator
    else:
        return 0
