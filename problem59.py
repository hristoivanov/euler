import time
from collections import Counter
start=time.time()

with open('p059_EncText.txt') as f:
	    content = f.readlines()

content = content[0].replace("\n",'')
content = content.split(',')
enc1 = []
enc2 = []
enc3 = []

for x in range(0,len(content),3):
	enc1.append(content[x])
for x in range(1,len(content),3):
	enc2.append(content[x])
for x in range(2,len(content),3):
	enc3.append(content[x])

enc1=Counter(enc1)
enc2=Counter(enc2)
enc3=Counter(enc3)
enc1= enc1.most_common(3)[0]
enc2= enc2.most_common(3)[0]
enc3= enc3.most_common(3)[0]

enc1 = 32 ^ int(enc1[0])
enc2 = 32 ^ int(enc2[0])
enc3 = 32 ^ int(enc3[0])

sol = content
for x in range(0,len(content),3):
	sol[x]=int(sol[x])^ enc1
for x in range(1,len(content),3):
	sol[x]=int(sol[x])^ enc2
for x in range(2,len(content),3):
	sol[x]=int(sol[x])^ enc3

for letter in sol:
	print unichr(letter),
print
the_ans = sum(sol)
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
