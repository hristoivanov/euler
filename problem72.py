import math
import time
start=time.time()

the_ans = 0
the_objective = 1000001
phiList = [0,0] + [x for x in range(2, the_objective)]
nums = [True] * the_objective
nums[0], nums[1] = False, False

for x in range(2, the_objective, 2):
    nums[x] = False
    phiList[x] = phiList[x] >> 1

for x in range(3, the_objective, 3):
    nums[x] = False
    phiList[x] = (phiList[x] << 1 ) / 3

for x in range(5, the_objective, 5):
    nums[x] = False
    phiList[x] = (phiList[x] << 2 ) / 5

for x in range(7, the_objective):
    if nums[x]:
        phiList[x] -= 1 
        for y in range(x*2, the_objective, x):
            nums[y] = False
            phiList[y] = (phiList[y] / x) * (x-1)

the_ans = sum(phiList)

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
