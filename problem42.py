with open('p042_words.txt') as f:
	    content = f.readlines()
import time
start=time.time()

def calc_triangle(limit):
	curr=0
	num=0
	triangles=[]
	while True:
		curr+=1
		num+=curr
		if num>limit:
			return triangles
		triangles.append(num)


words=content[0].replace('"','').split(',')
# 1000/30 ==> 33.3 charracter word of Zets
trian_nums=calc_triangle(1000) 

the_ans=0
for word in words:
	word=[ord(let)-64 for let in word]
	if sum(word) in trian_nums:
		the_ans+=1


print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
