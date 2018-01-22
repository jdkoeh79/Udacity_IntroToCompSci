# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n > 1:
		return fibonacci(n - 1) + fibonacci(n - 2)


#print fibonacci(0) #>>> 0
#print fibonacci(1) #>>> 1
#rint fibonacci(2) #>>> 1
#print fibonacci(3) #>>> 2
#print fibonacci(4) #>>> 3
#print fibonacci(5) #>>> 5
#print fibonacci(6) #>>> 8
#print fibonacci(7) #>>> 13
#print fibonacci(15) #>>> 610
''' Warning: this first function takes upwards of 20 secs to compute input of 36 '''
''' Calculating fibonacci 36 calls this function fibonacci(33) times (3,524,578 times) '''
#print fibonacci(35) #>>> 14930352 


#print ''


#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

'''My first try (Ugly, I know!)'''

def fibonacci(n):
	first = 1
	second = 1
	fibo = 0
	count = 2
	if n == 0:
		fibo = 0
	elif n < 3:
		fibo = 1
	else:
		while count != n:
			fibo = first + second
			first = second
			second = fibo
			count += 1
	return fibo

first, second = 1, 2
print second
print first


'''print fibonacci(0) #>>> 0
print fibonacci(1) #>>> 1
print fibonacci(2) #>>> 1
print fibonacci(3) #>>> 2 
print fibonacci(4) #>>> 3
print fibonacci(5) #>>> 5
print fibonacci(6) #>>> 8
print fibonacci(7) #>>> 13
print fibonacci(8)
print fibonacci(9)
print fibonacci(10)'''
#print fibonacci(15) #>>> 610
'''print fibonacci(26) #>>> 3524578'''


#print ''


'''Dave's function'''
# https://classroom.udacity.com/courses/cs101/lessons/48756019/concepts/482999590923

'''def fibonacci(n):
	current = 0    #first fibonacci number
	after = 1    #second fibonacci number
	for i in range(0, n):    # for loop using range eliminates counting passes through a while loop
		current, after = after, current + after    # multiple assignment eliminates the need for 3rd variable (fibo)
	return current




# If rabbits didn't die and could freely reproduce, how long would it take them
# to take over the world?

mass_of_earth = 5.9722 * 10**24 #kilograms
mass_of_rabbit = 2 #kilograms per rabbit

n = 1
while fibonacci(n) * mass_of_rabbit < mass_of_earth:
	n = n + 1
years = n / 12
print n
print years
print fibonacci(n)'''