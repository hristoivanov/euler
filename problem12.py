import math
import time

def factors(num):
	factors=0
	for x in range(1, int(math.floor( math.sqrt(num)))):
		if num%x==0:
			factors+=2
	return factors
			
start=time.time()
x=0
triangle=0
while True:
	x+=1
	triangle+=x
	#For every prime number  that you are divisible by, the number of factors increases by two. I dont know why, but this works.
	if triangle%2!=0:
		continue
	if triangle%3!=0:
		continue
	if triangle%5!=0:
		continue
	if triangle%7!=0:
		continue
	if triangle%11!=0:
		continue
	if triangle%13!=0:
		continue
	if triangle%17!=0:
		continue
	
	facts=factors(triangle)
	print facts

	if facts >= 500:
		print 'Answer: '+`triangle`+' Time: '+`time.time()-start`
		break;
