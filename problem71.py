import time
start=time.time()

the_ans = -1
the_min = 1

for x in range(2, 1000000):
    nominator = (3.0/7.0) * x
    remaining = nominator - int(nominator)
    if remaining > the_min or remaining == .0:
        continue
    the_ans = int(nominator)

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
