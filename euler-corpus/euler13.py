def euler013(): # 関数euler013の定義
	q = [] # qに空のリストを代入
	a = str(sum(q)) # aにqの要素の総和の文字列表現を代入
	ret = "" # retに空文字列を代入
	for i, ch in enumerate(a): # chをaの各要素、iをその番号として
		if i < 10: # もしiが10未満であれば
			ret += ch # retにchを追加
	return ret # retを返す
def euler013_front_n_slice(s, n): # sとnを引数とする関数euler013_front_n_sliceを定義
	ret = "" # retに空文字列を代入
	for i, ch in enumerate(s): # chをsの各要素、iをその番号として
		if i < n: # もしiがn未満であれば
			ret += ch # retにchを追加
	return ret # retを返す
def euler013_query_n_sum(q, n): # qとnを引数とする関数euler013_query_n_sumを定義
	s = 0 # sに0を代入
	for i in range(n): # n未満の非負整数を順にiとして
		s += q[i] # sにqのi番目を足す
	return s # sを返す
