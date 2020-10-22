def euler004(): # 関数euler004の定義
	ans = 0 # ansに0を代入
	for j in range(999, 99, -1): # 99より大きく999以下の整数を大きい方から順にjとして
		for i in range(999, 99, -1): # 99より大きく999以下の整数を大きい方から順にiとして
			s = (str)(j * i) # sにjとiの積の文字列表現を代入
			a = "" # aに空文字列を代入
			b = "" # bに空文字列を代入
			sep = (int)(len(s) / 2) + (len(s) % 2) # sepにsの長さを2で割った商とsを2で割った余りの和を代入
			for k in range(sep): # sep未満の非負整数を順にkとして
				a += s[k] # aにsのk番目の要素を足す
				b += s[len(s) - k - 1] # bにsの後ろからk番目の要素を足す
			if a == b: # もしaとbが等しければ
				ans = max(ans, i * j) # ansと、iとjの積の大きい方を新しいansとする
	return ans # ansを返す
def euler004_n_slice(s, n): # sとnを引数とする関数euler004_n_sliceの定義
	ret = "" # retに空文字列を代入
	for i in range(n): # n未満の非負整数を順にiとして
		ret += s[i] # retにsのi番目の要素を足す
	return ret # retを返す
def euler004_n_bslice(s, n): # sとnを引数とする関数euler004_n_bsliceの定義
	ret = "" # retに空文字列を代入
	for i in range(n): # n未満の非負整数を順にiとして
		ret += s[len(s) - 1 - i] # retにsの後ろからi番目の要素を足す
	return ret # retを返す
def euler004_is_equal(a, b): # aとbを引数とする関数euler004_is_equalの定義
	return a == b # aとbが等しければTrue、そうでなければFalseを返す
def euler004_half_digit(n): # nを引数とする関数euler004_half_digitの定義
	s = (str)(n) # sにnの文字列表現を代入
	a = len(s) # aにsの長さを代入
	return (int)(a / 2) + (a % 2) # aを2で割った商とsを2で割った余りの和を返す
def euler004_multiple(a, b): # aとbを引数とする関数euler004_multipleを定義
	return a * b # aとbの積を返す
def euler004_multiple_a(a, b): # aとbを引数とする関数euler004_multiple_aの定義
	res = 0 # resに0を代入
	for i in range(b): # 以下の処理をb回繰り返す
		res += a # resにaを足す
	return res # resを返す
def euler004_string_reverse(s): # sを引数とする関数euler004_string_reverseの定義
	ret = "" # retに空文字列を代入
	for ch in reversed(s): # sの各要素を後ろから順にchとして
		ret += ch # retにchを足す
	return ret # retを返す
def euler004_is_palindromic(s): # sを引数とする関数euler004_is_palindromicの定義
	rs = "" # rsに空文字列を代入
	for ch in reversed(s): # sの各要素を後ろから順にchとして
		rs += ch # rsにchを足す
	return s == rs # sとrsが等しければTrue、そうでなければFalseを返す
