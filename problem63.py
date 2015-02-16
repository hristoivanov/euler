import time
start=time.time()

def get_sol():
	sol =0 
	curr=1
	while True:
		for x in range(1,10):
			num=x**curr
			if len(str(num))==curr:
				sol +=1
			if len(str(num))<curr and x==9:
				return sol
		curr +=1


the_ans=get_sol()
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
