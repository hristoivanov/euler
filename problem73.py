import time
start=time.time()

import sys
sys.setrecursionlimit(100000)

def do_count(ln, ld, dn, dd, limit):
    y = (ld + dd)/(ld*dn - dd*ln)

    if y > limit:
        return 0

    x = (1 + ln*y)/ld

    to_return = 1
    to_return += do_count(ln,ld,x,y, limit)
    to_return += do_count(x,y,dn,dd, limit)
    return to_return

the_ans = do_count(1,3,1,2,12000)

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
