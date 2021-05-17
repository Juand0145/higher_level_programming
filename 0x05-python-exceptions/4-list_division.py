#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    array = []

    for i in range(list_length):
        division = 0

        try:
            division = my_list_1[i] / my_list_2[i]

        except (IndexError):
            print("out of range")

        except (ZeroDivisionError):
            print("division by 0")

        except TypeError:
            print("wrong type")

        finally:
            array.append(division)

    return array
