import time
start=time.time()

triangles=[]
pentagonals=set()
hexagonals=set()

count=286
while True:
	trian=count*(count+1)/2
	if trian>10**10:
		break
	triangles.append(trian)
	count+=1

count=166
while True:
	penta=count*(3*count-1)/2
	if penta>10**10:
		break
	pentagonals.add(penta)
	count+=1


count=144
while True:
	hexa=count*(2*count-1)
	if hexa>10**10:
		break
	hexagonals.add(hexa)
	count+=1


for trian in triangles:
	if trian in pentagonals and trian in hexagonals:
		the_ans=trian
		break

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
