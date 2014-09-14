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

def are_perms(num1, num2, num3):
	aux1=set([letter for letter in str(num1)])
	aux2=set([letter for letter in str(num2)])
	aux3=set([letter for letter in str(num3)])
	if aux1==aux2 and aux2==aux3:
		return True
	return False


primes=generate_primes(10000)
cool_primes=set()

for prime in primes:
	if prime >1000:
		cool_primes.add(prime)

for prime1 in cool_primes:
	for prime2 in cool_primes:
		if prime1>=prime2:
			continue
		if 2*prime2-prime1 in cool_primes:
			if are_perms(prime1, prime2, 2*prime2-prime1)==True:
				if prime1==1487:
					continue
				the_ans=str(prime1)+str(prime2)+str(2*prime2-prime1)


print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
