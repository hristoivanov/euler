from collections import Counter
import time
start=time.time()

def get_sol():
	curr = 0
	num = 0
	numbers = {}
	num_digits = 1
	while True:
		curr+=1
		num=curr**3
		if len(str(num)) > num_digits:
			num_digits +=1
			pos_solutions=[]
			for key in numbers:
				if numbers[key][0]==5:
					pos_solutions.append(numbers[key][1])
			if len(pos_solutions) != 0:
				return min(pos_solutions)
			numbers={}
		ord_digits=int("".join(sorted(str(num), reverse=True)))
		if numbers.has_key(ord_digits):
			numbers[ord_digits][0]+=1
		else:
			numbers[ord_digits]=[1,num]


the_ans=get_sol()
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
