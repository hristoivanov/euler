import math
import time
start=time.time()

def calc_digit(num, pos):
	pos_fact=math.factorial(pos)
	res=num/pos_fact
	rem=num%pos_fact
	return res, rem


def calc_perm(num, digits):
	if len(digits)==1:
		return str(digits.pop())

	res, rem=calc_digit(num, len(digits)-1)
	digit=str(digits.pop(res))
	return digit+ calc_perm(rem, digits)



digits=[x for x in range(0,10)]
the_ans=calc_perm(999999, digits)
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
