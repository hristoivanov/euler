with open('p022_names.txt') as f:
	    content = f.readlines()

import time
start=time.time()

names=content[0].replace('"','').split(',')
names=sorted(names)

pos=1
the_ans=0
for name in names:
	name_score=0
	for letter in name:
		name_score+=ord(letter)-64
	the_ans+=name_score*pos
	pos+=1

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
