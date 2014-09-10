import math
import time
start=time.time()

def calc_digit(num, pos):
	pos_fact=math.factorial(pos)
	res=num/pos_fact
	rem=num%pos_fact
	return res, rem


def calc_perm(num, digits, hh):
	if len(digits)==1:
		return str(digits.pop())

	if hh==0:
		return ''

	res, rem=calc_digit(num, len(digits)-1)
	digit=str(digits.pop(res))
	return digit+ calc_perm(rem, digits, hh-1)

def gen_pan_numbers(num_digits):
	lim=math.factorial(9)
	step=math.factorial(9-num_digits)
	for x in range (0, lim, step):
		digits=[y for y in range(1,10)]
		yield calc_perm(x, digits, num_digits)

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


# len(a)+len(b)+len(a+b) must be equal to 9
digits_pan=9
combinations=[]
for x in range(1,8):
	for y in range(1,8):
		if x+y-1==digits_pan-x-y  or  x+y==digits_pan-x-y:
			combinations.append([x,y])

# Remove the repeated 
combinations=combinations[:len(combinations)/2]

solution=set()
for comb in combinations:
	x, y=comb[0], comb[1]
	for a in gen_pan_numbers(x):
		for b in gen_pan_numbers(y):
			product=int(a)*int(b)
			if is_pandigital(a+b+str(product)):
				solution.add(product)

the_ans=sum(solution)
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
