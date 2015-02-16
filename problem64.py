import time
start=time.time()

def get_aux(num, aux, nom, den):
	nomm=nom
	denn=den
	den=(num-(denn)**2)/nomm
	nom=(-aux+(aux-denn)%den)
	return (nom, den)

def aux(num):
	curr=0
	while True:
		if (curr+1)**2 > num:
			break
		curr+=1
	if  curr**2 == num:
		return 0

	toople = (1, -curr)
	tooples=[toople]
	cont = 1
	while True:
		toople = get_aux(num, curr, toople[0], toople[1])
		toople = (toople[1], toople[0]) 
		if toople in tooples:
			break
		cont +=1
		tooples.append(toople)
	return cont

the_ans =0
for x in range (2, 10001):
	if aux(x)%2!=0:
		the_ans+=1

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
