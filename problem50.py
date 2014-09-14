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


primes=generate_primes(1000000)
primes2=sorted(list(primes))

the_max=0
enough=primes2.index(4001)
for x in range(0, 5):
	the_sum=primes2[x]
	for y in range(x+1, enough):
		the_sum+=primes2[y]
		if y-x < the_max:
			continue
		if the_sum in primes:
			if y-x>the_max:
				the_ans=the_sum
				the_max=y-x
				continue
		if the_sum>1000000:
			break


print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
