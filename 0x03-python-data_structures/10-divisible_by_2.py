#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisible_in_2 = []

    if not my_list:
        return None

    for number in my_list:
        if number % 2 == 0:
            divisible_in_2.append(True)

        else:
            divisible_in_2.append(False)

    return (divisible_in_2)
