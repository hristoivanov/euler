import time
start=time.time()
def isPrime(num):
	if num<=3: return num>=2
	if num%2 ==0 or num%3==0: return False
	for x in range (5, int(num**0.5)+1, 6):
		if num%x == 0 or num%(x+2)==0:
			return False
	return True

sqrs=1
prime_sqr=0
curr=1
the_ans=0
for leng in range(3, 10000000, 2):
	for x in range(0,4):
		curr +=leng-1
		sqrs+=1
		if isPrime(curr):
			prime_sqr+=1
	if prime_sqr*10 < sqrs:
		the_ans=leng
		break

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
