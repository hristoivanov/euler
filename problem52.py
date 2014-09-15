import time
start=time.time()

def same_digits(num1, num2):
	num1=sorted(list(str(num1)))
	num2=sorted(list(str(num2)))
	if num1==num2:
		return True
	return False

def special_number(num):
	for x in range(6,1, -1):
		if not(same_digits(num, num*x)):
			return False
	return True

posible_sol=[]
for x in range(1,6):
	for y in range(10**x,2*(10**x)):
		posible_sol.append(y)

for the_num in posible_sol:
	if special_number(the_num):
		the_ans=the_num
		break

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
