def my_fact(num):
	if num==0:
		return 1

	return num*my_fact(num-1)

import time
start=time.time()

aux=my_fact(100)
the_ans=0
for x in str(aux):
	the_ans+=int(x)

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`

# Alternative way to calculate factorial
import math
start=time.time()

aux=math.factorial(100)
the_ans=0
for x in str(aux):
	the_ans+=int(x)

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
