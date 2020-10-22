def euler006(): # 関数euler006の定義
	sumofsq = 0 # sumofsqに0を代入
	for i in range(100): # 100未満の非負整数を小さい方から順にiとして
		sumofsq += (i + 1) * (i + 1) # sumofsqにi+1の自乗を足す
	sqofsum = 101 * 50 # sqofsumに101と50の積を代入
	return sumofsq - sqofsum # sumofsqとsqofsumの差を返す
def euler006_make_common_diff_sequence(s, d, n): # sとdとnを引数とする関数euler006_make_common_diff_sequenceの定義
	ret = [s] # retにsのみからなるリストを代入
	for i in range(n - 1): # 以下の処理をn-1回繰り返す
		ret.append(ret[-1] + d) # retの末尾要素にdを加えたものをretの末尾に追加する
	return ret # retを返す
def euler006_make_common_diff_sequence_a(s, d, n): # sとdとnを引数とする関数euler006_make_common_dif_sequence_aの定義
	ret = [] # retを空リストとする
	for i in range(s, s + (d * n), d): # sからd個飛ばしでn個の整数をiとして
		ret.append(i) # retにiを追加
	return ret # retを返す
def euler006_n_square(n): # nを引数とする関数euler006_n_sequenceの定義
	return n * n # nの自乗を返す
def euler006_n_square_a(n): # nを引数とする関数euler006_n_square_aの定義
	ret = 0 # retに0を代入
	for i in range(n): # 以下の処理をn回繰り返す
		ret += n # retにnを足す
	return ret # retを返す
def euler006_sum_a_to_b(a, b): # aとbを引数とする関数euler006_sum_a_to_bの定義
	s = 0 # sに0を代入
	while a < b: # aがbより小さい間
		s += a # sにaを足す
		a += 1 # aに1を足す
	return s # sを返す
def euler006_sum_a_to_b_a(a, b): # aとbを引数とする関数euler006_sum_a_to_b_aの定義
	return sum(range(a, b)) # a以上b未満の整数の総和を返す
