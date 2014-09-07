def my_fact(num):
	if num==0:
		return 1

	return num*my_fact(num-1)

aux=my_fact(100)
print aux


the_ans=0
for x in str(aux):
	the_ans+=int(x)

print the_ans 


# Alternative way to calculate factorial
import math
print math.factorial(100)
