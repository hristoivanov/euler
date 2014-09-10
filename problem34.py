import time
start=time.time()

def my_fact(digit):
	if digit=='0':return 1
	if digit=='1':return 1
	if digit=='2':return 2
	if digit=='3':return 6
	if digit=='4':return 24
	if digit=='5':return 120
	if digit=='6':return 720
	if digit=='7':return 5040
	if digit=='8':return 40320
	if digit=='9':return 362880

def digit_fact_sum(num):
	num=str(num)
	the_sum=0
	for dig in num:
		the_sum+=my_fact(dig)

	return the_sum


the_ans=0
limit=9*my_fact('9')
# We dont use the actual limit beacuse the chances are so small for numbers bigger that 1 milion
for x in range(3,1000000):
	if x==digit_fact_sum(x):
		the_ans+=x

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
