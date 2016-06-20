import time
start=time.time()

the_ans = 0
the_objective = 1000001
phiList = list(range(the_objective))
nums = [True] * the_objective

for x in range(2, the_objective, 2):
    nums[x] = False
    phiList[x] >>= 1

for x in range(3, the_objective):
    if nums[x]:
        phiList[x] -= 1 
        for y in range(x*2, the_objective, x):
            nums[y] = False
            phiList[y] -= (phiList[y] / x)

the_ans = sum(phiList)-1

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
