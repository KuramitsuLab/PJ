def euler008(): # 関数euler008の定義
	sl = [] # slを空リストとする
	for i in range(5): # 5未満の非負整数iについて
		sl.append(int(s[i])) # slにsのi番目の要素の表す整数を追加
	m = 1 # mを1とする
	for i in sl: # sl内の各要素をiとして
		m *= i # mにiを掛ける
	for i in range(5, len(s)): # 5からsの要素数未満の整数iについて
		sl.append(int(s[i])) # slにsのi番目の要素の表す整数を追加
		sl.pop(0) # slの最初の要素を削除する
		a = 1 # aを1とする
		for j in sl: # sl内の各要素をjとして
			a *= j # aにjを掛ける
		m = max(m, a) # mとaの大きい方を新しいmとする
	return m # mを返す
def euler008_all_product(l): # lを引数とする関数euler008_all_productの定義
	ret = 1 # retを1とする
	for x in l: # l内の全ての要素xについて
		ret *= x # retにxを掛ける
	return ret # retを返す
def euler008_list_slice(l, s, c): # lとsとcを引数とする関数euler008_list_sliceの定義
	ret = [] # retを空のリストとする
	for i in range(c): # c未満の非負整数iについて
		ret.append(l[s + i]) # lのs+i番目の要素をretに追加する
	return ret # retを返す
def euler008_elem_max(a, b): # aとbを引数とする関数euler008_elem_maxの定義
	return b if a < b else a # bがaより大きければb、そうでなければaを返す
def euler008_elem_max_a(a, b): # aとbを引数とする関数euler008_elem_max_aの定義
	return max(a, b) # aとbの大きい方を返す
def euler008_list_add(l, a): # lとaを引数とする関数euler008_list_addの定義
	tmp = [a] # tmpをaのみからなるリストとする
	l += tmp # lの末尾にtmpを結合する
	return l # lを返す
def euler008_list_add_a(l, a): # lとaを引数とする関数euler008_list_add_aの定義
	l.append(a) # lの末尾にaを追加する
	return l # lを返す
