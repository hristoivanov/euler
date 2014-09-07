import calendar
import time
c=calendar.TextCalendar(calendar.MONDAY)

count=0
for x in range(1901, 2001):
	for y in range(1,13):
		aux=c.itermonthdays2(x,y)
		for z in aux:
			if z[0]==0:
				continue
			if z[1]==6:
				count+=1
			break;

print count
