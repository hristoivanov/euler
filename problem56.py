import time
start=time.time()

the_ans=0
for a in range(0,100):
	for b in range(0,100):
		num=sum(map(int,str(a**b)))
		if num > the_ans:
			the_ans=num

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
