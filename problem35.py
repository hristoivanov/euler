import math
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

def get_rotations(num):
	aux=str(num)
	for x in range(0, len(str(num))-1):
		aux=aux[-1]+aux[:-1]
		yield int(aux)

def is_special_prime(primes, prime):
	for rot in get_rotations(prime):
		if not(rot in primes):
			return False
	
	return True

primes = generate_primes(1000000)
the_ans=0
for prime in primes:
	if is_special_prime(primes, prime):
		the_ans+=1

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
