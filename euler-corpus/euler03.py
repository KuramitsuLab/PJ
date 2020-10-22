def euler003(): # 関数euler003の定義
	n = 600851475143 # nに600851475143を代入
	i = 2 # iに2を代入
	while i * i < n: # iの自乗がn未満の間
		while n % i == 0: # nがiで割り切れる間
			n = n / i # nをiで割る
		i = i + 1 # iに1を足す
	return int(n) # nを整数にした結果を返す
def euler003_n_morethan_square(a, n): # aとnを引数とする関数euler003_n_morethan_squareの定義
	return a * a < n # aの自乗がnより小さければTrue、そうでなければFalseを返す
def euler003_n_divide_a(n, a): # nとaを引数とする関数euler003_n_divide_aの定義
	while n % a == 0: # nがaで割り切れる間
		n /= a # nをaで割る
	return int(n) # nを整数にした結果を返す
