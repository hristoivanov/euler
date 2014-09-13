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

def is_special(primes, num):
	for x in range (1,100):
		if num-2*x**2 in primes:
			return False
	
	return True

primes=generate_primes(10000)
the_max=max(primes)

count=7
while True:
	count+=2
	if count>the_max:
		print 'Insuficient primes :('
	if count in primes:
		continue
	if is_special(primes, count):
		the_ans=count
		break

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`

