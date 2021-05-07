#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0

    roman_dictionary = {'I': 1, 'V': 5, 'X': 10,
                        'L': 50, 'C': 100,
                        'D': 500, 'M': 1000}

    translate = 0

    n_characters = len(roman_string)

    for j in range(n_characters):
        if j > 0 and roman_dictionary[roman_string[j]]\
             > roman_dictionary[roman_string[j - 1]]:
             
            translate += roman_dictionary[roman_string[j]]\
                 - 2 * roman_dictionary[roman_string[j-1]]

        else:
            translate += roman_dictionary[roman_string[j]]

    return translate
