# Write your solution for 1.4 here!

def is_prime(x):
	i = 2
	while i < x:
		if x%i > 0:
			i += 1
		elif x%i == 0:
			print ("is prime")

is_prime(14)


