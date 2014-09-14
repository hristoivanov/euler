import time
start=time.time()


def sieve(num, composites, primes, target):
	if num in composites:
		return
	primes.add(num) 
	for i in range(num, target, num)[1:]:
		composites.add(i)

def generate_primes(target):
	composites = set([])
	primes = set([])
	for p in range(2, target):
    		sieve(p, composites, primes, target)
	return primes

def get_num_prime_factor(primes, num):
	count=0
	for prime in primes:
		rem=num%prime
		if rem==0:
			count+=1
	return count

primes=generate_primes(1000)

the_set=set()
for x in range(20,250000):
	if get_num_prime_factor(primes, x)==4:
		the_set.add(x)


from operator import itemgetter
from itertools import groupby
data = sorted(the_set)
for k, g in groupby(enumerate(data), lambda (i,x):i-x):
	    the_map=map(itemgetter(1), g)
	    if len(the_map)==4:
		    the_ans=the_map[0]
		    break

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
