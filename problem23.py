import math
def is_abundant(num):
	# The use of a set for 'divisors' slow us.
	divisors=[1]
	for x in range(2, int(math.floor( math.sqrt(num)))+1):
		if num%x==0:
			divisors.append(x)
			res=num/x
			if res!=x:
				divisors.append(res)
	if sum(divisors)>num:
		return True
	return False

def calc_abundants():
	abundants=[]
	for x in range(12,28123+1):
		if is_abundant(x):
			abundants.append(x)
	return abundants



import time
start=time.time()

# First of all, this will help us understand the code.
# Even+Even=Even
# Odd+Odd=Even
# Odd+Even=Odd

# First of all we calculate all the abundant numbers.
abundants=calc_abundants()
# More of the abundant numbers are even, there is a few odd abundant numbers

# First we discart the even numbers that cant be expressed as a sum of two abundant numbers.
# The diference between consecutive even abundant numbers is as much 6 and most of the times 4 or 2.
# This make easy to express most of the even numbers as a sum of two abundant numbers
unreachable=set([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 26, 28, 34, 46])
# All the other even numbers can be expressed as a sum of two abundant numbers

# We will add all the odd numbers and then we will remove the one that we arent interested in.
odd=1
while True:
	unreachable.add(odd)
	odd+=2
	if odd>28123:
		break;



# Separate the even and odd abundant numbers
abundants_odd=set()
abundants_even=set()
for num in abundants:
	if num%2!=0:
		abundants_odd.add(num)
	else:
		abundants_even.add(num)


# Calculate all the odd numbers that can be expressed as a sum of two abundant numbers
for odd in abundants_odd:
	for even in abundants_even:
		the_bad=odd+even
		if the_bad>28123:
			break
		unreachable.discard(the_bad)

# Finally print the answer
the_ans= sum(unreachable)
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
