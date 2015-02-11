def get_aux(iters):
	if iters == 0:
		return 0,1,2
	ans, nom ,den = get_aux(iters-1)
	aux_nom =nom+den
	if len(str(aux_nom)) > len(str(den)):
		ans+=1
	return ans, den, nom+2*den 

import time
start=time.time()
import sys
sys.setrecursionlimit(1100)

the_ans, nom, den=get_aux(1000)
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
