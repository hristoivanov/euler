def sum_divisors(num):
	divisors=[]
	if num==1:
		return 1
	for x in range(1,num):
		if num%x==0:
			divisors.append(x)
	return sum(divisors)

sum_divs={}
for x in range(1,10000):
	sum_divs[x]=sum_divisors(x)

the_ans=0
for x in sum_divs:
	if sum_divs.has_key(sum_divs[x]):
		if x==sum_divs[sum_divs[x]]:
			if x!=sum_divs[x]:
				the_ans+=x
	else:
		aux=sum_divisors(sum_divs[x])
		if x==aux:
			the_ans+=x
print the_ans
