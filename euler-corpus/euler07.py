def euler007(): # 関数euler007の定義
	count = 0 # countを0とする
	p = 1 # pを1とする
	pl = [] # plを空のリストとする
	while count < 10001: # countが10001未満である間
		p += 1 # pに1を足す
		l = [ i for i in range(2, int(math.sqrt(p)) + 1) if p % i == 0 ] # 2からpの平方根までの整数iのうち、pを割り切ることができるもののリストをlに代入
		if len(l) == 0: # もしlが空なら
			count += 1 # countに1を足す
	return p # pを返す
def euler007_n_division(a, n): # aとnを引数とする関数euler007_n_difisionの定義
	return a % n == 0 # aがnで割り切れるならTrue、そうでないならFalseを返す
def euler007_n_division_a(a, n): # aとnを引数とする関数euler007_n_division_aの定義
	while a > 0: # aが0より大きい間
		a -= n # aからnを引く
	return a == 0 # aが0であればTrue、そうでなければFalseを返す
def euler007_is_prime(a): # aを引数とする関数euler007_is_primeの定義
	dl = [] # dlを空リストとする
	for i in range(2, a): # 2以上a未満の整数を順にiとして
		if a % i == 0: # aがiで割り切れるなら
			dl.append(i) # dlにiを追加
	return len(dl) == 0 # dlが空であればTrue、そうでなければFalseを返す
def euler007_is_prime_a(a): # aを引数とする関数euler007_is_prime_aの定義
	if a < 2: # もしaが2未満であれば
		return False # Falseを返す
	elif a == 2: # そうでなく、もしaが2であれば
		return True # Trueを返す
	else: # いずれでもなければ
		for i in range(2, int(a**0.5) + 1): # 2からaの平方根までの整数を順にiとして
			if a % i == 0: # もしaがiで割り切れれば
				return False # Falseを返す
		return True # Trueを返す
def euler007_succ(a): # aを引数とする関数euler007_succの定義
	return a + 1 # aに1を足した数を返す
def euler007_is_less(a, b): # aとbを引数とする関数euler007_is_lessの定義
	return a < b # aがbより小さければTrue、そうでなければFalseを返す
def euler007_is_equale_zero(a): # aを引数とする関数euler007_is_equale_zeroの定義
	return a == 0 # aが0であればTrue、そうでなければFalseを返す
