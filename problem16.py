import time
start=time.time()
power=2**1000
answer=0
for x in str(power):
	answer+= int(x)
print 'Answer: '+`answer`+' Time: '+`time.time()-start`
