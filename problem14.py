def next(aux):
	if aux%2==0:
		return aux/2
	return 3*aux+1

def chain_lenght(aux, known):
	if aux==1:
		return 1
	if known.has_key(aux):
		return known[aux]
	return chain_lenght(next(aux), known)+1

import time
start=time.time()

known={}
the_max=0
the_ans=0
for x in range(1,1000*1000):
	lenght=chain_lenght(x, known)
	known[x]=lenght
	if the_max<lenght:
		the_max=lenght
		the_ans=x

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
