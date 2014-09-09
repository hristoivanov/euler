import time
start=time.time()


the_ans=1
count=1
for x in range(3, 1002, 2):
	for y in range(0, 4):
		count+=x-1
		the_ans+=count

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
