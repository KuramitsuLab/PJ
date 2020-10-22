def euler002(): # 関数euler002の定義
	fib = [1, 2] # fibに1と2からなるリストを代入
	while fib[-1] < 4000000: # fibの末尾要素が4000000未満の間繰り返し
		fib.append(fib[-1] + fib[-2]) # fibの末尾要素とその次の要素を足してfibの末尾に追加する
	s = 0 # sに0を代入
	for x in fib: # fibの各要素を前から順にxとして
		if x % 2 == 0: # xが2でわりきれるなら
			s += x # sにxを足す
	return s # sを返す
def euler002_divide_2(n): # nを引数とする関数euler002_divide_2の定義
	return n % 2 == 0 # nが2で割り切れる場合True、そうでなければFalseを返す
def euler002_add_param(a, b): # aとbを引数とする関数euler002_add_paramの定義
	return a + b # aとbの和を返す
def euler002_sum_list(l): # lを引数とする関数euler002_sum_listの定義
	s = 0 # sに0を代入
	for x in l: # lの各要素を順にxとして
		s += x # sにxを足す
	return s # sを返す
def euler002_sum_list_a(l): # lを引数とする関数euler002_sum_list_aの定義
	return sum(l) # lの全要素の総和を返す
def euler002_n_fibnocci_sequence(n): # nを引数とする関数euler002_n_fibonacci_sequenceの定義
	fibs = [0, 1] # fibsに0と1からなるリストを代入
	a = n - 2 # aにnから2を引いた数を代入
	if n == 1: # もしnが1であれば
		return [0] # 0のみからなるリストを返す
	else: # そうでなければ
		while a > 0: # aが0より大きい間
			fibs.append(fibs[-1] + fibs[-2]) # fibsの末尾要素とその次の要素を足してfibsの末尾に追加
			a -= 1 # aから1を引く
		return fibs # fibsを返す
def euler002_n_fibnocci_number(n): # nを引数とする関数euler002_n_fibonacci_numberの定義
	fibs = [0, 1] # fibsに0と1からなるリストを代入
	if 0 < n <= 2: # もしnが0より大きく、かつ2以下であるなら
		return fibs[n - 1] # fibsのn-1番目の要素を返す
	else: # そうでなければ
		a = n - 2  # aにnから2を引いた数を代入
		while a > 0: # aが0より大きい間
			fibs.append(fibs[-1] + fibs[-2]) # fibsの末尾要素とその次の要素を足してfibsの末尾に追加
			a -= 1 # aから1を引く
		return fibs[-1] # fibsの末尾要素を返す
