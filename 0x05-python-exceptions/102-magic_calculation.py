#!/usr/bin/python3
def magic_calculation(a, b):
    result_operation = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')

            else:
                result_operation += a ** b / i

        except:
            result_operation = b + a
            break

    return result_operation
