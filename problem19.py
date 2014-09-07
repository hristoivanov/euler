import calendar
import time
start=time.time()
c=calendar.TextCalendar(calendar.MONDAY)

the_ans=0
for x in range(1901, 2001):
	for y in range(1,13):
		aux=c.itermonthdays2(x,y)
		for z in aux:
			if z[0]==0:
				continue
			if z[1]==6:
				the_ans+=1
			break;

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
