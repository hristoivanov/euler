one_nine = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten_nineteen=['ten', 'eleven', 'thelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
twenty_ninety = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundred='hundred'
thousand='thousand'
andd='and'

the_sum=0
for x in one_nine:
	the_sum+=len(x)
	print x

for x in ten_nineteen:
	the_sum+=len(x)
	print x

for x in twenty_ninety:
	the_sum+=len(x)
	print x
	for y in one_nine:
		the_sum+=len(x)+len(y)
		print x+'-'+y


for x in one_nine:
	the_sum+=len(x+hundred)
	print x+hundred
	for y in one_nine:
		the_sum+=len(x+hundred+andd+y)
		print x+hundred+andd+y

	for y in ten_nineteen:
		the_sum+=len(x+hundred+andd+y)
		print x+hundred+andd+y

	for y in twenty_ninety:
		the_sum+=len(x+hundred+andd+y)
		print x+hundred+andd+y
		for z in one_nine:
			the_sum+=len(x+hundred+andd+y+z)
			print x+hundred+andd+y+'-'+z
	
the_sum+=len('one'+thousand)
print 'one'+thousand
print the_sum
