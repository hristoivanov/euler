import time
start=time.time()

def fibonacci(num1, num2):
	return num2, num1+num2


num1, num2= 1, 1
x=2
while True:
	num1, num2=fibonacci(num1, num2)
	x+=1
	if len(str(num2))==1000:
		break

the_ans=x
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`


# Answer from the people of the internet that know more mathematics than me
phi=1.6180339887498
from math import log
#  The nth Fibonacci number is [phi**n / sqrt(5)], where the
#  brackets denote "nearest integer".
#  So we need phi**n/sqrt(5) > 10**999

n = (999 * log(10) + log(5) / 2) / log(phi)
print round(n)

