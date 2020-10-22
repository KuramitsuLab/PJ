def euler014(): # 関数euler014の定義
	N = 10**6 # Nに10の6乗を代入
	cl = [-1] * N # clにN個の-1を要素とするリストを代入
	cl[1] = 0 # clの2番目の要素を0とする
	for n in range(2, N): # 2からN未満の各数を順にnとして
		b = [] # bに空リストを代入
		while n >= N or cl[n] == -1: # nがN以上かclのn番目が-1である間
			b.append(n) # bの末尾にnを追加
			n = int(n / 2) if n % 2 == 0 else n * 3 + 1 # nが2で割り切れる場合nを2で割った商を、そうでない場合nの3倍に1を足した数をnに代入
		l = cl[n] # lにclのn番目の要素を代入
		for m in reversed(b): # bの要素を末尾から順にmとして繰り返し
			l += 1 # lに1を足す
			if m < N: # もしmがN未満なら
				cl[m] = l # clのm番目をlにする
	m = 0 # mに0を代入
	ret = 0 # retに0を代入
	for i, n in enumerate(cl): # clの各要素をn、iを番号として繰り返し
		if m < n: # もしmがnより小さい場合
			m = n # mをnにする
			ret = i # retをiにする
	return ret # retを返す
def euler014_collatz_calc(n): # nを引数とする関数euler014_collatz_calcを定義
	return int(n / 2) if n % 2 == 0 else n * 3 + 1 # nが2で割り切れるならnを2で割った商を、そうでないならnの3倍に1を足した数を返す
def euler014_collatz_problem_count(n): # nを引数とする関数euler014_collatz_problem_countを定義
	c = 0 # cに0を代入
	while n != 1: # nが1でない間
		n = int(n / 2) if n % 2 == 0 else n * 3 + 1 # nが2で割り切れるならnを2で割った商を、そうでないならnの3倍に1を足した数を新しいnとする
		c += 1 # cに1を足す
	return c # cを返す
def euler014_list_init(l, n): # lとnを引数とする関数euler014_list_initを定義
	ret = [] # retを空リストとする
	for i in range(l): # 以下の処理をl回繰り返す
		ret.append(n) # retの末尾にnを追加する
	return ret # retを返す
def euler014_list_enum(l): # lを引数とする関数euler014_list_enumを定義
	ret = [] # retを空リストとする
	for i in range(len(l)): # lの各要素の番号を順にiとして
		ret.append((i, l[i])) # retにiとlのi番目からなる組を追加する
	return ret # retを返す
def euler014_list_reverse(l): # lを引数とする関数euler014_list_reverseを定義
	ret = [] # retを空リストとする
	for i in reversed(l): # lの末尾要素から順にiとして
		ret.append(i) # retの末尾にiを追加する
	return ret # retを返す
def euler014_make_range_list(s, e): # sとeを引数とする関数euler014_make_range_listを定義
	ret = [] # retを空とする
	for i in range(s, e): # s以上e未満の整数を小さい方からiとして
		ret.append(i) # retの末尾にiを追加する
	return ret # retを返す
