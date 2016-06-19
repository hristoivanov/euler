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


primesList = generate_primes(4000)
primesList = [x for x in primesList if x > 2000]
the_ans = 1
the_min = 10

for x in range(len(primesList)-1, -1, -1):
    for y in range(x, len(primesList)):
        the_num = primesList[x] * primesList[y]
        if x == y:
            phi_num = the_num - primesList[x]
        else:
            phi_num = the_num * (   1.0 
                                    - (1.0/float(primesList[x])) 
                                    - (1.0 - 1.0/float(primesList[x])) * 1.0/float(primesList[y]))
            phi_num = int(round(phi_num))

	aux1 = sorted([letter for letter in str(the_num)])
        aux2 = sorted([letter for letter in str(phi_num)])

        if aux1 == aux2 and the_num<10**7:
            if the_min > the_num/float(phi_num):
                the_min = the_num/float(phi_num)
                the_ans = the_num
        

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
