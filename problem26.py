import time
import sys
sys.setrecursionlimit(90000)
start=time.time()


def calc_digit(num, div):
	digit=num/div
	num=(num%div)*10
	return digit, num

def calc_division(num, div, max_digit, curr_digit=0, result=[]):
	for x in range(0, max_digit):
		if num==0:
			return result

		digit, num=calc_digit(num, div)
		result.append(digit)

	return result

def len_cycle(digits, max_digit_len):
	if len(digits)<max_digit_len:
		return 0
	for x in range(1, max_digit_len/2):
		if digits[-x:]==digits[-x*2:-x]:
			return x

	return -1
	print 'Error insuficient max_digit_len'


max_digit_len=2000
solution=0
max_len=0
for x in range(1, 1000):
	digits=calc_division(1, x, max_digit_len, 0, [])
	the_len=len_cycle(digits, max_digit_len)
	if the_len>max_len:
		solution=x
		max_len=the_len

the_ans=solution
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
