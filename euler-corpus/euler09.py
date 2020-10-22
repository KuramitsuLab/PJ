def euler009(): # 関数euler009の定義
	for i in range(1, 1000): # 1以上1000未満の整数iについて
		for j in range(i, 1000): # i以上1000未満の整数jについて
			for k in range(j, 1000): # j以上1000未満の整数kについて
				p = i * i + j * j # pにiの自乗とjの自乗の和を代入
				if p == k * k and i + j + k == 1000: # もしpがkの自乗と等しく、かつiとjとkの和が1000であれば
					return i * j * k # iとjとkの積を返す
def euler009_is_pythagoras(a, b, c): # aとbとcを引数とする関数euler009_is_pythagorasの定義
	return a * a + b * b == c * c # aの自乗とbの自乗がcの自乗と等しければTrue、そうでなければFalseを返す
def euler009_n_square(n): # nを引数とする関数euler009_n_squareの定義
	return n * n # nの自乗を返す
def euler009_n_square_a(n): # nを引数とする関数euler009_n_square_aの定義
	ret = 0 # retに0を代入する
	for i in range(n): # 以下の処理をn回繰り返す
		ret += n # retにnを足す
	return ret # retを返す
def euler009_is_sum_equation1000(tp): # tpを引数とする関数euler009_is_sum_equation1000の定義
	s = 0 # sに0を代入
	for x in tp: # tpの各要素をxとして
		s += x # sにxを足す
	return s == 1000 # sが1000ならばTrue、そうでなければFalseを返す
def euler009_is_sum_equation1000_a(tp): # tpを引数とする関数euler009_is_sum_equation1000_aの定義
	return sum(tp) == 1000 # tpの各要素の総和が1000と等しければTrue、そうでなければFalseを返す
def euler009_all_product(l): # lを引数とする関数euler009_all_productの定義
	ret = 1 # retを1とする
	for a in l: # l内の全要素aについて
		ret *= a # aをretに掛ける
	return ret # retを返す
