import time
start=time.time()

def generate_primes(target):
	nums = [True] * target
	nums[0], nums[1] = False, False
	for x in range(4, target, 2):
		nums[x] = False
	root_limit = int(target**.5)+1
	for x in range(3,root_limit):
		if nums[x]:
			for y in range(x*x, target, 2*x):
				nums[y] = False

	primes=set()
	for x in range(2, len(nums)):
		if nums[x]:
			primes.add(x)
	return primes

def has_rep_digits(num):
	aux=len(set([x for x in str(num)]))
	if aux<len(str(num)):
		return True
	return False

def get_rep_digits(num):
	num=str(num)
	dig_reps=set()
	for x in range(0, len(num)):
		for y in range(0, len(num)):
			if x==y:
				continue
			if num[x]==num[y]:
				dig_reps.add(num[x])
	return dig_reps

def get_eight_prime_family(primes):
	for prime in primes:
		if has_rep_digits(prime):
			for rep_digit in get_rep_digits(prime):
				count=0
				the_nums=[]
				for x in range(0, 10):
					if x-count>3:
						break
					the_num=str(prime)
					the_num=the_num.replace(rep_digit,str(x))
					if int(the_num) in primes:
						the_nums.append(the_num)
						count+=1
				if count>=8:
					if the_nums[0][0]=='0':
						continue
					return the_nums[0]



primes=generate_primes(1000000)
primes=set(sorted(primes))
the_ans=get_eight_prime_family(primes)
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
