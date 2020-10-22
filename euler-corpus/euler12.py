def euler012(): # 関数euler012の定義
	s = 1 # sに1を代入
	c = 0 # cに0を代入
	pl = [2] # plに2のみからなるリストを代入
	fl = [1] * 4 + [0] * 96 # flに1が4個と0が96個繋がったリストを代入
	while c < 500: # cが500未満である間
		tn = sum(range(1, s + 1)) # tnに1からsの総和を代入
		if not s % 2: # もしsが2で割り切れるなら
			t = (int(s / 2), s + 1) # tにsを2で割った商とs+1の組を代入
		else: # そうでなければ
			t = (s, int((s + 1) / 2)) # tにsとs+1を2で割った商の組を代入
		fc = 1 # fcに1を代入
		for x in t: # t内の各要素をxとして
			if len(fl) < x: # もしflの長さがxより小さければ
				l = [0] * (x - len(fl) + 1) # lに0を(x-flの長さ+1)回繰り返したリストを代入
				fl += l # flにlを代入
			if not fl[x]: # もしflのx番目が偽であれば
				nc = 1 # ncに1を代入
				for i in range(pl[-1], x + 1): # plの末尾要素からxまでの数を順にiとして
					for j in range(2, int(x**0.5) + 1): # 2からxの平方根までの数を順にjとして
						if i % j == 0: # もしiがjで割り切れるなら
							break # ループから抜ける
					else: # ループが最後まで処理された場合
						if not i in pl: # plにiが含まれていなければ
							pl.append(i) # plにiを追加する
				for i in pl: # pl内の各要素をiとして
					if i > int(tn / 2): # もしiがtnの半分よりも大きければ
						break # ループから抜ける
					if x % i == 0: # もしxがiで割り切れるなら
						j = 1 # jを1にする
						a = tn # aをtnにする
						while a % i == 0: # aがiで割り切れる間
							a /= i # aをiで割る
							j += 1 # jに1を足す
						else: # ループが正常に終了した場合
							nc *= j # ncにjを掛ける
				fl[x] = nc # flのx番目の要素をncにする
			fc *= fl[x] # fcにflのx番目の要素を掛ける
		s += 1 # sに1を足す
		c = fc # cをfcにする
	return tn # tnを返す
def euler012_a_over_b(a, b): # aとbを引数とする関数euler012_a_over_bの定義
	return b < a # bがaより小さければTrue、そうでなければFalseを返す
def euler012_range_prime_enumerate(s, e): # sとeを引数とする関数euler012_range_prime_enumerateの定義
	pl = [] # plに空リストを代入
	if s <= 1: # もしsが1以下であれば
		s = 2 # sを2にする
	for i in range(s, e + 1): # sからeまでの数を順にiとして
		f = True # fにTrueを代入
		for j in range(2, int(i**0.5) + 1): # 2からiの平方根までの数を順にjとして
			if i % j == 0: # もしiがjで割り切れるなら
				break # ループを抜ける
		else: # ループが正常に終了した場合
			pl.append(i) # plにiを追加する
	return pl # plを返す
def euler012_is_coprime(a, b): # aとbを引数とする関数euler012_is_coprimeの定義
	while b != 0: # bが0でない間
		a, b = b, a % b # aにbを、bにaをbで割った余りを代入
	return a == 1 # aが1であればTrue、そうでなければFalseを返す
def euler012_count_division(n, a): # nとaを引数とする関数euler012_count_divisionの定義
	ret = 0 # retに0を代入
	while n % a == 0: # nがaで割り切れる間
		n /= a # nをaで割る
		ret += 1 # retに1を足す
	return ret # retを返す
def euler012_prime_factorize(n): # nを引数とする関数euler012_prime_factorizeの定義
	primes = [True] * (n + 1) # primesにn+1個のTrueからなるリストを代入
	p = [] # pに空リストを代入
	for i in range(2, int(n**0.5) + 1): # 2からnの平方根までの数を順にiとして
		if primes[i]: # もしprimesのi番目が真であれば
			for j in range(i + i, n + 1, i): # iの倍からnまでの数をi個飛ばしで順にjとして
				primes[j] = False # primesのj番目をFalseにする
	for i in range(2, n + 1): # 2からnまでの数を順にiとして
		if primes[i]: # もしprimesのi番目が真なら
			p.append(i) # pの末尾にiを追加する
	fl = [] # flに空リストを代入
	for x in p: # p内の各要素を順にxとして
		if n % x == 0: # もしnがxで割り切れるなら
			a = n # aをnとする
			c = 0 # cを0とする
			while a % x == 0: # aがxで割り切れる間
				a /= x # aをxで割る
				c += 1 # cに1を足す
			else: # ループが終了したら
				fl.append((x, c)) # xとcの組をflに追加する
	return fl # flを返す
def euler012_nth_triangular_number(n): # nを引数とする関数euler012_nth_triangular_numberを定義
	return sum(range(1, n + 1)) # 1からnまでの整数の総和を返す
def euler012_next_triangular_number(tn): # tnを引数とする関数euler012_next_triangular_numberを定義
	ret = 0 # retに0を代入
	c = 1 # cに1を代入
	while ret <= tn: # retがtn以下の間繰り返し
		ret += c # retにcを足す
		c += 1 # cに1を足す
	return ret # retを返す
def euler012_count_divisor(expl): # explを引数とする関数euler012_count_divisorを定義
	ret = 1 # retに1を代入
	for x in expl: # explの各要素をxとして
		ret *= (x + 1) # retにx+1を掛ける
	return ret # retを返す
def euler012_is_list_empty(l): # lを引数とする関数euler012_is_list_emptyを定義
	return not l # lが偽であればTrue、そうでなければFalseを返す
def euler012_is_list_empty_a(l): # lを引数とする関数euler012_is_list_empty_aを定義
	return len(l) == 0 # lの長さが0であればTrue、そうでなければFalseを返す
