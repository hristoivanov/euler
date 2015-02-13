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

def isPrime(num):
	if num<=3: return num>=2
	if num%2 ==0 or num%3==0: return False
	for x in range (5, int(num**0.5)+1, 6):
		if num%x == 0 or num%(x+2)==0:
			return False
	return True

def check(nums):
	for num in nums[:-1]:
		if not isPrime(int(str(nums[-1])+str(num))): return False
		if not isPrime(int(str(num)+str(nums[-1]))): return False
	return True

primes=generate_primes(10000)
#primes=sorted(primes)
def getTheNum():
	for prime1 in primes:
		for prime2 in primes[::-1]:
			if prime1 >= prime2: continue
			if not check([prime1, prime2]):continue
			for prime3 in primes:
				if prime2 >= prime3: continue
				if not check([prime1, prime2, prime3]):continue
				for prime4 in primes[::-1]:
					if prime3 >= prime4: continue
					if not check([prime1, prime2, prime3, prime4]):continue
					for prime5 in primes:
						if prime4 >= prime5: continue
						if not check([prime1, prime2, prime3, prime4, prime5]):continue
						print prime1,prime2,prime3,prime4,prime5
						return prime1+prime2+prime3+prime4+prime5


print getTheNum()
the_ans=0
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
