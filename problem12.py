import math
import time
x=0
triangle=0
while True:
	x+=1
	triangle+=x

	if triangle%2!=0:
		continue
	if triangle%3!=0:
		continue
	if triangle%5!=0:
		continue
	if triangle%7!=0:
		continue
	if triangle%11!=0:
		continue
	if triangle%13!=0:
		continue
	if triangle%17!=0:
		continue
	
	factors=0
	the_factors=[]
	for y in range(1,int(math.floor(triangle))):
		if triangle % y==0:
			factors+=1
			the_factors.append(y)


	print `triangle`+' has '+`factors+1`+' facors...'+`the_factors[:]`
	if factors >= 500:
		print `triangle`+' has '+`factors+1`+' facors...'+`the_factors[:]`
		break;
