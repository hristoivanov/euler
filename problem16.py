import time
start=time.time()
power=2**1000
the_ans=0
for x in str(power):
	the_ans+= int(x)
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
