import time
start=time.time()

theNum = 100
aux = [1]*theNum

cache = {}

def mReduce(numbers, limit):
    l = r = 0

    cacheKey = str(limit)+str(numbers)
    if cacheKey in cache:
        return cache[cacheKey]

    if len(numbers) > 2:
        if numbers[0] > numbers[1]:
            sumTheSecondAndThird = [numbers[1]+numbers[2]] + numbers[3:]
            l = mReduce(sumTheSecondAndThird, numbers[0])

    if len(numbers) >= 2:
        sumTheFirstTwo = [numbers[0]+numbers[1]] + numbers[2:]
        if  limit >= sumTheFirstTwo[0]:
            r = mReduce(sumTheFirstTwo, limit)

    to_return = 1 + l + r
    cache[cacheKey] = to_return
    return to_return

the_ans = mReduce(aux, theNum) -1
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
