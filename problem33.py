import time
start=time.time()

def remove_common(a, b):
	a, b=str(a), str(b)
	if a[0]=='0' or a[1]=='0' or b[0]=='0' or b[1]=='0':
		return 1.0, 99.0
	if a[0]==b[1]:
		return float(a[1]), float(b[0])
	if a[1]==b[0]:
		return float(a[0]), float(b[1])
	return 1.0,99.0 

solution=[]
for x in range(12,100):
	for y in range(12,100):
		x=float(x)
		y=float(y)
		if x==y:
			continue
		xx, yy= remove_common(x, y)
		if x/y == xx/yy:
			solution.append([int(x), int(y)])

solution=solution[:len(solution)/2]

num, dem=1,1
for sol in solution:
	num*=sol[0]
	dem*=sol[1]


the_ans=`num`+'/'+`dem`
print 'This should be enough, no need to reduce the fraction.'
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
