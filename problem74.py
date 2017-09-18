import time
start=time.time()

def get_digit_fact_chain(x, digit_fact_chain, digit_fact, evaluated=set()):
    if x in digit_fact_chain:
        return digit_fact_chain[x]
    if x in evaluated:
        return 0

    evaluated.add(x)
    aux = 0
    for y in str(x):
        aux += digit_fact[int(y)]
    to_return = 1 + get_digit_fact_chain(aux, digit_fact_chain, digit_fact, evaluated)
    digit_fact_chain[x] = to_return
    return to_return

digit_fact_chain = {}
the_ans = 0
digit_fact = [1]*10
current_fact = 1
for x in range(1,10):
    current_fact *= x
    digit_fact[x] = current_fact

for x in range(1, 1000000):
    aux = get_digit_fact_chain(x, digit_fact_chain, digit_fact)
    if aux == 60:
        the_ans += 1

print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
