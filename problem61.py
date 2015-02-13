import itertools
import time
start=time.time()

def get_nums():
	n=0
	numbers = [set([]), set([]), set([]), set([]), set([]), set([])]
	while True:
		n+=1
		nums	= [0,0,0,0,0,0]
		nums[0]	= n*(n+1)/2
		nums[1]	= n**2
		nums[2]	= n*(3*n-1)/2
		nums[3]	= n*(2*n-1)
		nums[4]	= n*(5*n-3)/2
		nums[5]	= n*(3*n-2)
		for x,num in enumerate(nums):
			if x==0 and num > 9999: return numbers
			if num < 1000: continue
			if num > 9999: continue
			numbers[x].add(num)

cont=0
def are_cool(num1, num2):
	global cont
	cont +=1
	if str(num1)[2:]==str(num2)[:2]:
		return True
	return False


def get_sol1():
	numbers = get_nums()
	for k in itertools.permutations('012345'):
		for y0 in numbers[int(k[ 0])]:
			for y1 in numbers[int(k[ 1])]:
				if not are_cool(y0, y1): continue
				for y2 in numbers[int(k[2])]:
					if not are_cool(y1, y2): continue
					for y3 in numbers[int(k[3])]:
						if not are_cool(y2, y3): continue
						for y4 in numbers[int(k[4])]:
							if not are_cool(y3, y4): continue
							for y5 in numbers[int(k[5])]:
								if not are_cool(y4, y5): continue
								if not are_cool(y5, y0): continue
								return y1+y2+y3+y4+y5+y0

#Faster
def get_sol():
	numbers = get_nums()
	for x1, set1 in enumerate(numbers):
		for y1 in set1:
			for x2, set2 in enumerate(numbers):
				if x2==x1:continue
				for y2 in set2:
					if not are_cool(y1, y2): continue
					for x3, set3 in enumerate(numbers):
						if x3==x2:continue
						if x3==x1:continue
						for y3 in set3:
							if not are_cool(y2, y3): continue
							for x4, set4 in enumerate(numbers):
								if x4==x3:continue
								if x4==x2:continue
								if x4==x1:continue
								for y4 in set4:
									if not are_cool(y3, y4): continue
									for x5, set5 in enumerate(numbers):
										if x5==x4:continue
										if x5==x3:continue
										if x5==x2:continue
										if x5==x1:continue
										for y5 in set5:
											if not are_cool(y4, y5): continue
											for x6, set6 in enumerate(numbers):
												if x6==x5:continue
												if x6==x4:continue
												if x6==x3:continue
												if x6==x2:continue
												if x6==x1:continue
												for y6 in set6:
													if not are_cool(y5, y6): continue
													if not are_cool(y6, y1): continue
													return y1+y2+y3+y4+y5+y6
			

the_ans=get_sol()
print cont
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
