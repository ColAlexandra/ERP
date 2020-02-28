""" Common module
implement commonly used functions here
"""

import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''

    for i in range(8):
        
        if i == 0 or i == 5:
            lucky_char = 'abcdefghijklmnopqrstuvwxyz'
        elif i == 1 or i == 4:
            lucky_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif i == 2 or i == 3:
            lucky_char = '0123456789'
        else:
            lucky_char = '!@#$%^&*()-=+<>'
        
        generated += random.choice(lucky_char)
        
    for i in range(len(table)):
        if generated == table[i][0]:
            generate_random(table)

    return generated
