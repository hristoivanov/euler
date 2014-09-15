import time
start=time.time()

def gen_factorials(target):
	factorials=[1 for x in range(0,target+1)]
	for x in range(1,len(factorials)):
		factorials[x]=x*factorials[x-1]
	return factorials

factorials=gen_factorials(100)

the_ans=0
for x in range(1,101):
	for y in range(x,0,-1):
		if factorials[x]/(factorials[y]*factorials[x-y])>10**6:
			the_ans+=1

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
