aux=["75"
,"95 64"
,"17 47 82"
,"18 35 87 10"
,"20 04 82 47 65"
,"19 01 23 75 03 34"
,"88 02 77 73 07 63 67"
,"99 65 04 28 06 16 70 92"
,"41 41 26 56 83 40 80 70 33"
,"41 48 72 33 47 32 37 16 94 29"
,"53 71 44 65 25 43 91 52 97 51 14"
,"70 11 33 28 77 73 17 78 39 68 17 57"
,"91 71 52 38 17 14 91 43 58 50 27 29 48"
,"63 66 04 68 89 53 67 30 73 16 69 87 40 31"
,"04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"]

import time
start=time.time()

aux2=[]
for x in aux:
	aux2.append(x.split(' '))


aux3=[]
for x in aux2:
	aux4=[]
	for y in x:
		aux4.append(int(y))
	aux3.append(aux4)

#Extend
for x in aux3:
	for y in xrange(0,len(aux3)-len(x)):
		x.append(0)
	
the_array=aux3

def the_sum(posx, posy):
	if posy<0 or posy>len(the_array)-1:
		return -1000

	if posx==len(the_array)-1:
		return the_array[posx][posy]

	return the_array[posx][posy]+max(the_sum(posx+1,posy), the_sum(posx+1,posy+1))


ans=the_sum(0,0)
print 'Answer: '+`ans`+' Time: '+`time.time()-start`
