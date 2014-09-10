import time
start=time.time()

def is_pandigital(num):
	if '0' in num:
		return False
	if len(num)!=9:
		return False
	digits=set()
	for digit in num:
		digits.add(digit)
	if len(digits)==9:
		return True
	return False

# 9{1,2,3,4,5}==>918273645 a value we know. 
# Our number must start with 9
# x1    	 9X   9XX    9XXX
# x2   		1XX  1XXX   1XXXX
# x3   		2XX  2XXX
# x4   		3XX
# sum_digits	 11    11      9
# valid?         NO    NO     OK


for x in range(9000,10000):
	if is_pandigital(str(x)+str(2*x)):
		the_ans=int(str(x)+str(2*x))

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
