# 5-2.2 Shift n Letters.py
# Lesson 5 Problem Set (Optional): 2/3

# Quiz: Shift n Letters


# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be alphabet_positive,
# negative or zero.


def shift_n_letters(letter, n):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']
    letter_pos = alphabet.index(letter)
    if letter_pos + n > 25:
        return alphabet[0 + ((letter_pos + n) - 26)]
    return alphabet[letter_pos + n]



print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i