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

def calc_digit(num, pos):
	pos_fact=math.factorial(pos)
	res=num/pos_fact
	rem=num%pos_fact
	return res, rem


def calc_perm(num, digits):
	if len(digits)==1:
		return str(digits.pop())

	res, rem=calc_digit(num, len(digits)-1)
	digit=str(digits.pop(res))
	return digit+ calc_perm(rem, digits)

def gen_pan_numbers(num_digits):
	for x in range (math.factorial(num_digits)-1, -1, -1):
		digits=[y for y in range(1,num_digits+1)]
		yield calc_perm(x, digits)

# We cant be 100% sure of this method. The more primes we use the better
def is_prime(primes, num):
	for prime in primes:
		if int(num)%prime==0:
			return False

	return True

def get_pan_prime(primes):
	pos_primes=[]
	for x in range(9,3,-1):
		if sum([x for x in range(1,x+1)])%3==0:
			continue
		for pan in gen_pan_numbers(x):
			if is_prime(primes, pan):
				return int(pan)



primes=generate_primes(10000)
the_ans=get_pan_prime(primes)
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
