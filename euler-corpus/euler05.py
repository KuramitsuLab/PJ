def euler005(): # 関数euler005の定義
	prime = [] # primeに空のリストを代入
	for i in range(2, 20): # 2から20未満の整数を順にiとして
		l = [] # lに空リストを代入
		for y in prime: # primeの各要素をyとして
			if i % y == 0: # もしiがyで割り切れるなら
				l.append(y) # lにyを追加する
		if len(l) == 0: # もしlの長さが0であれば
			prime.append(i) # primeにiを追加する
	a = 1 # aに1を代入
	for p in prime: # primeの各要素をpとして
		for i in range(int(20**(1/p))): # 20の1/p乗未満の非負整数を順にiとして
			a = a * p # aにpを掛ける
	return a # aを返す
def euler005_enum_prime(n): # nを引数とする関数euler005_enum_primeの定義
	prime = [] # primeに空リストを代入
	for i in range(2, n + 1): # 2からnまでの各整数を順にiとして
		f = True # fにTrueを代入
		for j in prime: # prime内の各要素をjとして
			if i % j == 0: # iがjで割り切れるなら
				f = False # fをFalseにする
				break # ループから抜ける
		if f: # fがTrueであれば
			prime.append(i) # primeにiを追加する
	return prime # primeを返す
def euler005_enum_prime_a(n): # nを引数とする関数euler005_enum_prime_aの定義
	primes = [] # primesを空リストとする
	for i in range(2, n + 1): # 2からnまでの各整数を順にiとして
		if i == 2: # iが2であれば
			primes.append(i) # primesにiを追加する
		else: # そうでなければ
			for j in range(2, int(i**0.5) + 1): # 2からiの平方根までの整数をjとして
				if i % j == 0: # iがjで割り切れるなら
					break # ループを抜ける
			else: # ループが正常に終了した場合
				primes.append(i) # primesにiを追加する
	return primes # primesを返す
def euler005_enum_prime_b(n): # nを引数とする関数euler005_enum_prime_bの定義
	primes = [True] * (n + 1) # primesをTrueがn+1個繋がったリストとする
	ret = [] # retを空リストとする
	for i in range(2, int(n**0.5) + 1): # 2からnの平方根までの整数をiとして
		if primes[i]: # もしprimesのi番目がTrueであれば
			for j in range(i + i, n + 1, i): # iの自乗からnまでのi個飛ばしの整数をjとして
				primes[j] = False # primesのj番目をFalseにする
	for i in range(2, n + 1): # 2からn+1までの整数を順にiとして
		if primes[i]: # もしprimesのi番目がTrueであれば
			ret.append(i) # retにiを追加する
	return ret # retを返す
def euler005_expmax(p, n): # pとnを引数とする関数euler005_expmaxの定義
	a = 1 # aに1を代入
	while a < n: # aがnより小さい間
		a *= p # aにpを掛ける
	return int(a / p) # a割るpの整数部分を返す
def euler005_expmax_a(p, n): # pとnを引数とする関数euler005_expmax_aの定義
	return p**int(n**(1/p)) # pの(nのp乗根の整数部分)乗を返す
