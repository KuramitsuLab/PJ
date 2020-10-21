import random

c = 0
n = 0

for i in range(n):
	x = random.random()
	y = random.random()
	if x**2 + y**2 < 1.0:
		c += 1
	elif x == 0:
		continue
print(c/4*n)

def fibo(n):
	if n < 3: return 1
	return fibo(n-1) + fibo(n-2)
