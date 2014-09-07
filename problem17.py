one_nine = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten_nineteen=['ten', 'eleven', 'thelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
twenty_ninety = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundred='hundred'
thousand='thousand'
andd='and'

import time
start=time.time()

the_ans=0
for x in one_nine:
	the_ans+=len(x)

for x in ten_nineteen:
	the_ans+=len(x)

for x in twenty_ninety:
	the_ans+=len(x)
	for y in one_nine:
		the_ans+=len(x)+len(y)


for x in one_nine:
	the_ans+=len(x+hundred)
	for y in one_nine:
		the_ans+=len(x+hundred+andd+y)

	for y in ten_nineteen:
		the_ans+=len(x+hundred+andd+y)

	for y in twenty_ninety:
		the_ans+=len(x+hundred+andd+y)
		for z in one_nine:
			the_ans+=len(x+hundred+andd+y+z)
	
the_ans+=len('one'+thousand)
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
