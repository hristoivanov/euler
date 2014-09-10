import time
start=time.time()

# Must pass string
def is_palin(num):
	if len(num)==1:
		return True
	# Python things
	if num[:len(num)/2]==num[-(len(num)/2):][::-1]:
		return  True
	return False

the_ans=0
for x in range(1, 1000000):
	the_bin=bin(x)[2:]
	if is_palin(str(x)) and is_palin(the_bin):
		the_ans+=x

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
