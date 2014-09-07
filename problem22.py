with open('p022_names.txt') as f:
	    content = f.readlines()

names=content[0].replace('"','').split(',')
names=sorted(names)

pos=1
total_score=0
for name in names:
	name_score=0
	for letter in name:
		name_score+=ord(letter)-64
	total_score+=name_score*pos
	pos+=1

print total_score
