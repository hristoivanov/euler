import time
start=time.time()

def combinations(total, coins):
	solution=0
	if coins==[1]:
		return 1
	for x in range(0, total+1, coins[0]):
		solution+=combinations(total-x, coins[1:])

	return solution

coins=[200, 100, 50, 20, 10, 5, 2, 1]
the_ans=combinations(200, coins)
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
