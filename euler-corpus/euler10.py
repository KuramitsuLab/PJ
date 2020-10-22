def euler010(): # 関数euler010の定義
	p = [True] * 2000000 # pにTrueのみからなるリストを代入
	for x in range(2, int(2000000**0.5) + 1): # xを2から2000000の0.5乗までの間で変化させて繰り返し
		if p[x]: # もしpのx番目が真であれば
			for i in range(2 * x, len(p), x): # iをxの2倍からpの長さ未満までxごとに変化させて繰り返し
				p[i] = False # pのi番目にFalseを代入
	ret = [] # retに空のリストを代入
	for i in range(2, 2000000): # iを2から2000000まで変化させて繰り返し
		if p[i]: # もしpのi番目が真であれば
			ret.append(i) # retの末尾にiを追加
	return sum(ret) # retの要素の総和を返す
def euler010_enum_prime(n): # 引数nを取る関数euler010_enum_primeの定義
	p = [True] * n # Trueがn個並んでいるリストをpに代入
	for x in range(2, int(n**0.5) + 1): # xを2からnの平方根の範囲で変化させて繰り返し
		if p[x]: # pのx番目が真であれば
			for i in range(2 * x, len(p), x): # iをxの2倍からpの長さまでx単位で変化させて繰り返し
				p[i] = False # pのi番目をFalseにする
	ret = [] # retに空のリストを代入
	for i in range(2, n): # iを2以上n未満の間で増加させながら繰り返し
		if p[i]: # もしpのi番目が真であれば
			ret.append(i) # retの末尾にiを追加
	return ret # retを返す
def euler010_n_is_prime(n): # nを引数とする関数euler010_n_is_primeの定義
	judge = True # judgeにTrueを代入
	if n < 2: # もしnが2より小さければ
		return False # Falseを返す
	elif n == 2: # そうでなくて、もしnが2であれば
		return True # Trueを返す
	for i in range(2, int(n**0.5) + 1): # iを2以上nの平方根以下の間で繰り返し
		if judge and n % i == 0: # もしjudgeが真でかつnがiで割り切れるなら
			judge = False # judgeをFalseにする
	return judge # judgeを返す
def euler010_list_sum(l): # lを引数とする関数euler010_list_sumの定義
	s = 0 # sに0を代入
	for x in l: # lに含まれる各要素をxに代入して繰り返し
		s += x # sにxを足す
	return s # sを返す
def euler010_list_sum_a(l): # lを引数とする関数euler010_list_sum_aの定義
	return sum(l) # l内の要素の総和を返す
def euler010_n_multiple_list(s, e, d): # s,e,dを引数とする関数euler010_n_multiple_listの定義
	ret = [] # retに空のリストを代入
	while s < e: # sがeより小さい間繰り返し
		ret.append(s) # retの末尾にsを追加する
		s += d # sにdを足す
	return ret # retを返す
