import time
start=time.time()

solution=set()
for x in range(2,101):
	for y in range(2,101):
		solution.add(x**y)

the_ans=len(solution)
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
