# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?


""" Recursive (function called in it's own definition).  These are considered""" 
""" expensive in Python and a non-recursive method should be used when possible. """

def is_palindrome(s):
    if s == '':
        return True
    else:
    	if s[0] == s[-1]:
    		return is_palindrome(s[1:-1])
    	else:
    		return False
 

print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True





""" Iterative (a for loop) """

def iter_palindrome(s):
	for i in range(0, len(s) / 2):
		if s[i] != s[-(i + 1)]:
			return False
	return True


print iter_palindrome('')
#>>> True
print iter_palindrome('abab')
#>>> False
print iter_palindrome('abba')
#>>> True