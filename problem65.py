def get_aux(iters, curr=1):
	if iters == curr:
		if curr%3==0:
			return 1,2*curr/3
		return 1,1
	nom ,den = get_aux(iters, curr+1)
	if curr==1:
		return 2*den+nom, den
	if curr%3==0:
		return den, nom+(2*curr/3)*den
	return den, nom+den


import time
start=time.time()

nom, den=get_aux(100)
the_ans= sum( [int(x) for x in str(nom)])
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
