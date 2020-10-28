import random

c = 0  # {{カウンタ}}
n = 100

for i in range(n):
	# 乱数を生成する
	# まじか

	x = random.random()
	y = random.random()
#困った
	if x**2 + y**2 < 1.0: # 原点からの距離が1未満のとき
		c += 1

print(c*4/n)

def fibo(n): # {{n番目のフィボナッチ数}}
	if n < 3: return 1
	return fibo(n-1) + fibo(n-2)
