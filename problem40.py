import time
start=time.time()

aux=[9*x*10**(x-1) for x in range(1,6)]
aux2=[aux[x]/(x+1) for x in range(0,5)]
limit=(10**6-sum(aux))/6
limit+=sum(aux2)+1

solution=[]
for x in range(1,limit+1):
	solution.extend(str(x))

the_ans=int(solution[0])*int(solution[9])*int(solution[99])*int(solution[999])*int(solution[9999])*int(solution[99999])*int(solution[999999])
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
