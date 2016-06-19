import time
start=time.time()

def generate_primes(target):
	nums = [True] * target
	nums[0], nums[1] = False, False
	for x in range(4, target, 2):
		nums[x] = False
	root_limit = int(target**.5)+1
	for x in range(3, root_limit):
		if nums[x]:
			for y in range(x*x, target, 2*x):
				nums[y] = False

	primes=[]
	for x in range(2, len(nums)):
		if nums[x]:
			primes.append(x)
	return primes


primesList = generate_primes(100)

the_ans = 1
for prime in primesList:
    aux = the_ans * prime
    if aux > 10**6:
        break
    the_ans = aux

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
