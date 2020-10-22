def euler016(): # 関数euler016の定義
	q = str(2**1000) # qに2の1000乗の文字列表現を格納
	s = 0 # sに0を代入
	for x in q: # qの各要素を前から順にxとして
		s += int(x) # sにxを表す整数を足す
	return s # sを返す
def euler016_all_digit_sum(n): # nを引数とする関数euler016_all_digit_sumの定義
	q = str(n) # qにnの文字列表現を格納
	s = 0 # sに0を代入
	for ch in q: # qの各要素を前から順にchとして
		s += int(ch) # sにchの表す整数を足す
	return s # sを返す
def euler016_n_separate_digit(n): # nを引数とする関数euler016_n_separate_digitの定義
	ret = [n % 10] # retをnを10で割った余りのみからなるリストとする
	while int(n / 10) > 0: # nを10で割った整数部分が0でない間繰り返し
		n = int(n / 10) # nを10で割った整数部分を新しいnとする
		ret.insert(0, n % 10) # retの先頭にnを10で割った余りを追加する
	return ret # retを返す
def euler016_a_exp_b(a, b): # aとbを引数とする関数euler016_a_exp_bの定義
	res = 1 # resを1とする
	c = 0 # cを0とする
	while c < b: # cがbより小さい間
		res *= a # resにaを掛ける
		c += 1 # cに1を足す
	return res # resを返す
def euler016_a_exp_b_a(a, b): # aとbを引数とする関数euler016_a_exp_b_aの定義
	return a**b # aのb乗を返す
