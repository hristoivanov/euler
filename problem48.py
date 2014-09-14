import time
start=time.time()

the_ans=0
for x in range(1,1000):
	the_ans+=x**x

the_ans=str(the_ans)[-10:]

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
