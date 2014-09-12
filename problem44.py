import math
import time
start=time.time()

# x(3x-1)/2 -y(3y-1)/2 = z(3z-1)/2
# z=1/6(1+sqrt(1 -12x +36x^2 +12y -36y^2))
# Rest
def special(x,y):
	return 1.0/6.0*(1.0+math.sqrt( 1  -12*x  +36*x**2  +12*y  -36*y**2))

# x(3x-1)/2 +y(3y-1)/2 = z(3z-1)/2
# z=1/6(1+sqrt(1 -12x +36x^2 -12y +36y^2))
# Sum
def special2(x,y):
	return 1.0/6.0*(1.0+math.sqrt( 1  -12*x  +36*x**2  -12*y  +36*y**2))

# Using maths
def get_sol():
	for x in range(1, 10000):
		for y in range(1, x-1):
			if special(x,y).is_integer()  and  special2(x,y).is_integer():
				the_num=special(x,y)
				return (3*the_num**2 - the_num)/2
def gen_pentas(amount):
	pentas=[n*(3*n-1)/2 for n in xrange(1, amount+1)]
	return pentas, set(pentas)

# Using computer science
def get_sol2():
	pentas, penta_set=gen_pentas(5000)
	for x in range(0,5000):
		for y in range(0,x-1):
			the_sum=pentas[x]+pentas[y]
			the_rest=pentas[x]-pentas[y]
			if the_sum in penta_set and the_rest in penta_set:
				return the_rest

the_ans=get_sol2()
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
