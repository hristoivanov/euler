import time
start=time.time()

def len_cycle2(num):
	rest=10%num
	list_rests=[10]
	while True:
		rest=(rest%num)*10
		if rest==0:
			return 0
		if rest in list_rests:
			return len(list_rests)-list_rests.index(rest)
		list_rests.append(rest)



solution=0
max_len=0
for x in range(1, 1000):
	the_len=len_cycle2(x)
	if the_len>max_len:
		solution=x
		max_len=the_len

the_ans=solution
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
