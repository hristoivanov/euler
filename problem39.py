import math
import time
start=time.time()

values=[0 for x in range(0, 1001)]
for x in range(1,1000):
	for y in range(x,1000):
		c=math.sqrt(x**2 + y**2)
		if c.is_integer():
			p=x+y+int(c)
			if p<=1000:
				values[p]+=1

the_ans=values.index(max(values))
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
