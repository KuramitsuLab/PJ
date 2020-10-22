def euler019(): # 関数euler019の定義
	d = 365 # dに365を代入
	sd = 0 # sdに0を代入
	for y in range(1901, 2001): # 1901以上2001未満の整数を順にyとして
		for i, day in enumerate(days): # dayをdaysの各要素、iをその番号として
			if d % 7 == 6: # もしdを7で割った余りが6であれば
				sd += 1 # sdに1を足す
			d += day  # dにdayを足す
			if (y % 400 == 0 or ((not y % 100 == 0) and y % 4 == 0)) and i == 1: # yが400で割り切れるか、100で割り切れずに4で割り切れ、さらにiが1である場合、
				d += 1 # dに1を足す
	return sd # sdを返す
def euler019_is_leap_year(y): # yを引数とする関数euler019_is_leap_yearを定義
	return y % 400 == 0 or ((not y % 100 == 0) and y % 4 == 0) # yが400で割り切れるか、100で割り切れずに4で割り切れる場合True、そうでない場合Falseを返す。
def euler019_names_of_the_day(y, m, d): # yとmとdを引数とする関数euler019_names_of_the_dayを定義
	if m <= 2: # もしmが2以下であれば
		m += 12 # mに12を足す
		y -= 1 # yから1を引く
	gamma = 0 # gammaに0を代入
	if 1582 <= y: # もしyが1582以上であれば
		gamma = -2 * int(y / 100) + int( int(y / 100) / 4 ) # gammaにy/100の整数部分の-2倍とy/100の整数部分を4で割った整数部分の和を代入
	else: # そうでなければ
		gamma = -1 * int(y / 100) + 5 # gammaにyを100で割った整数部分の-1倍に5を足したものを代入
	h = (d + int(26 * (m + 1) / 10) + (y % 100) + int((y % 100) / 4) + gamma) % 7 # hにd、26(m+1)/10の整数部分、yyを100で割った余り、y%100/4の整数部分、gammaを足した結果を代入
	return name[h] # nameのh番目を返す
