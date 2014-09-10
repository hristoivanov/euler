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


def is_trunc_prime(primes, num):
	if num ==2 or num==3 or num==5 or num==7:
		return False
	for x in range(len(str(num))-1, 0, -1):
		if not(int(str(num)[:x]) in primes):
			return False
	for x in range(1, len(str(num)), 1):
		if not(int(str(num)[x:]) in primes):
			return False

	return True

primes = generate_primes(1000000)

count=0
the_ans=0
for prime in primes:
	if is_trunc_prime(primes, prime):
		count+=1
		the_ans+=prime
		if count==11:
			break

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
