import time

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

def num_generated_primes(a, b, primes):
	n=0
	aux=0
	while True:
		n+=1
		the_num=n**2+a*n+b
		if the_num<2:
			return n
		for prim in primes:
			if the_num%prim==0:
				if the_num!=prim:
					return n
				aux=-1
				break
		if aux!=-1:
			print the_num, 'More primes are needed'


start=time.time()

primes=sorted(generate_primes(10000))
# b can only take prime values
bb=sorted(generate_primes(1000))
the_max=0
solution=[]

# for n=1
# 1**2 + 1*a  + b
# odd  + odd  + odd =  odd
# odd  + even + odd = even  
# a must be odd....
for a in range(-999, 1000, 2):
	for b in bb:
		value=num_generated_primes(a, b, primes)
		if value > the_max:
			the_max=value
			solution=[a, b]


the_ans=solution[0]*solution[1]
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
