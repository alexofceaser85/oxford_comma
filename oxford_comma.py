#!/usr/bin/env python3

"""
prints a list of an array seperated by commas and the final word in the array
has a comma and begins with and
"""

__author__ = "Alex DeCesare"
__version__ = "20-August-2020"

MEAL = ["pizza", "hot wings", "greek salad", "ice cream"]

def parse_array_to_string(array_to_parse):
    """
    parses the array to a string
    """
    if array_to_parse:
        array_length = len(array_to_parse) - 1
        add_and_to_final_word = "and " +  array_to_parse[array_length]

        array_to_parse[array_length] = add_and_to_final_word

        the_meal = ', '.join(array_to_parse)
        print(the_meal)
    if not array_to_parse:
        print("Cannot parse an empty list")

parse_array_to_string(MEAL)
