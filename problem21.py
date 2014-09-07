import math
def sum_divisors(num):
	divisors=[1]
	if num==1:
		return 1
	for x in range(2, int(math.floor( math.sqrt(num)))):
		if num%x==0:
			divisors.append(x)
			divisors.append(num/x)

	return sum(divisors)

import time
start=time.time()

sum_divs={}
for x in range(1,10000):
	sum_divs[x]=sum_divisors(x)

the_ans=0
for x in sum_divs:
	if sum_divs.has_key(sum_divs[x]):
		if x==sum_divs[sum_divs[x]]:
			if x!=sum_divs[x]:
				the_ans+=x

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
