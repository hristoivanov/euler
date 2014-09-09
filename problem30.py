import time
start=time.time()

the_pow=5
limit =the_pow*9**the_pow

solution=0
for x in range(2, limit):
	digits=str(x)
	the_sum=0
	for digit in digits:
		the_sum+=int(digit)**the_pow

	if the_sum==x:
		solution+=x

the_ans=solution
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
