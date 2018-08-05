
# Write your solution for 1.3 here!

a = 0 
i = 1

#while a < 10000:
#	a += i
#	i += 1

while a < 10000 :
	if i% 2 == 0 :
		a += i 
		i += 1
	else :
		i += 1

print(a)
print(i)