import math
import time
start=time.time()

def is_pan(num):
	num=str(num)
	digits=set()
	for digit in num:
		digits.add(digit)

	if len(num)==len(digits):
		return True
	return False

multiples_17=[]
count=1
while True:
	the_num=count*17
	if the_num>1000:
		break
	count+=1
	if not(the_num in multiples_17):
		multiples_17.append(the_num)
		continue

multiples_13=[]
for mul_17 in multiples_17:
	for x in range(0, 1000, 100):
		# trim the last digit
		to_use=mul_17/10
		to_use+=x
		if to_use%13==0:
			multiples_13.append(to_use*10+mul_17%10)

multiples_11=[]
for mul_13 in multiples_13:
	for x in range(0, 1000, 100):
		# trim last 2 digits
		to_use=mul_13/100
		to_use+=x
		if to_use%11==0:
			if is_pan(to_use*100+mul_13%100):
				multiples_11.append(to_use*100+mul_13%100)
multiples_7=[]
for mul_11 in multiples_11:
	for x in range(0, 1000, 100):
		# trim last 2 digits
		to_use=mul_11/1000
		to_use+=x
		if to_use%7==0:
			if is_pan(to_use*1000+mul_11%1000):
				multiples_7.append(to_use*1000+mul_11%1000)

multiples_5=[]
for mul_7 in multiples_7:
	for x in range(0, 1000, 100):
		# trim last 2 digits
		to_use=mul_7/10000
		to_use+=x
		if to_use%5==0:
			if is_pan(to_use*10000+mul_7%10000):
				multiples_5.append(to_use*10000+mul_7%10000)
multiples_3=[]
for mul_5 in multiples_5:
	for x in range(0, 1000, 100):
		# trim last 2 digits
		to_use=mul_5/100000
		to_use+=x
		if to_use%3==0:
			if is_pan(to_use*100000+mul_5%100000):
				multiples_3.append(to_use*100000+mul_5%100000)
multiples_2=[]
for mul_3 in multiples_3:
	for x in range(0, 1000, 100):
		# trim last 2 digits
		to_use=mul_3/1000000
		to_use+=x
		if to_use%2==0:
			if is_pan(to_use*1000000+mul_3%1000000):
				multiples_2.append(to_use*1000000+mul_3%1000000)

# By now 0 must have been used
valid_mul_2=[]
for mul_2 in multiples_2:
	if len(str(mul_2))==9:
		valid_mul_2.append(mul_2)


solution=[]
for mul_2 in valid_mul_2:
	for x in range(1,10):
		to_use=mul_2+x*10**9
		if is_pan(to_use):
			solution.append(to_use)
	
the_ans=sum(solution)
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
