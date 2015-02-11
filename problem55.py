import time
start=time.time()

# Must pass string
def is_palin(num):
	num=str(num)
	if num == num[::-1]:
		return True
	return False

def get_reverse(num):
	return int(str(num)[::-1])
def get_next(num):
	return num+get_reverse(num)

the_ans=0
for x in range(1,10000):
	num = x
	for y in range (0,50):
		num=get_next(num)
		if is_palin(num):
			break
	if y == 49:
		the_ans+=1

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
