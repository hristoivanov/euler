#Pascal triangle
def paths2(num):
	num+=1
	solution = [[1 for x in xrange(0,num)] for x in xrange(0,num)]

	for y in xrange(0, num):
		for x in xrange(0, num):
			if x == 0 or y == 0:
				continue
			solution[y][x] = solution[y-1][x] + solution[y][x-1]

	return solution[num-1][num-1]

# Too slow
endx=10
endy=10
def paths(posx, posy):
	if posx==endx or posy==endy:
		return 1

	paths_right=paths(posx+1, posy)

	paths_down=paths(posx, posy+1)

	return paths_right+paths_down

import time
start=time.time()
the_ans=paths2(20)
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
