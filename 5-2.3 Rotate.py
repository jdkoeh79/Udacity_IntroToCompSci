# Lesson 5 Problem Set (Optional): 3/3

# Rotate

# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.


def shift_n_letters(letter, n):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']
    letter_pos = alphabet.index(letter)
    if letter_pos + n > 25:
        return alphabet[0 + ((letter_pos + n) - 26)]
    return alphabet[letter_pos + n]


def rotate(input, n):
	output = ""
	for item in input:
		if item == " ":
			output += item
		else:
			shifted = shift_n_letters(item, n)
			output += shifted
	return output

		




print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???