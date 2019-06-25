import time
start=time.time()


def isPrime(n, primes):
    for prime in primes:
        if n%prime == 0:
            return False
    return True


def mReduce(limit, numbers):
    cacheKey = str(limit)+'-'+str(numbers[0])
    if cacheKey in cache:
        return cache[cacheKey]

    to_return = 0
    for x in range(len(numbers)):
        num = numbers[x]
        if num > limit:
            break
        if num == limit:
            to_return += 1
        to_return += mReduce(limit-num, numbers[x:])

    cache[cacheKey] = to_return
    return to_return


primes = [2]
the_ans = 2
cache = {}

while True:
    the_ans += 1

    if isPrime(the_ans, primes):
        primes.append(the_ans)

    if mReduce(the_ans, primes) > 5000:
        break

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
