def euler017(): # 関数euler017の定義
	ret = 0 # retに0を代入
	for n in range(1, 1001): # 1から1001未満の数を順にnとして
		if n <= 20: # もしnが20以下であれば
			ret += len(word[n]) # retにwordのn番目の要素の長さを足す
		elif len(str(n)) == 2: # そうでなくて、もしnの文字列表現の長さが2であれば
			ret += len(twoword[int(n / 10)]) # towordのn/10番目の要素の長さをretに足す
			ret += len(word[n % 10]) # wordのn%10番目の要素の長さをretに足す
		elif len(str(n)) == 3: # そうでなくて、もしnの文字列表現の長さが3であれば
			ret += len(word[int(n / 100)]) # wordのn/100番目の要素の長さをretに足す
			ret += len("hundredand") # "hundredand"の文字数をretに足す
			a = n % 100 # aにnを100で割った余りを代入
			if a != 0 and a <= 20: # もしaが0でなくて、かつaが20以下であれば
				ret += len(word[a]) # retにwordのa番目の要素の長さを足す
			elif a == 0: # そうでなくて、もしaが0であれば
				ret -= 3 # retから3を引く
			else: # いずれでもなければ
				ret += len(twoword[int(a / 10)]) # retにtowordのa/10番目の要素の長さを足す
				ret += len(word[a % 10]) # retにwordのa%10番目の要素の長さを足す
		else: # 上記のいずれでもなければ
			ret += len("onethousand") # retに"onethousand"の文字数を足す
	return ret # retを返す
def euler017_digit_separate(n): # nを引数とする関数euler017_digit_separateの定義
	q = str(n) # qをnの文字列表現とする
	ret = [] # retを空リストとする
	for ch in q: # qの各要素を前から順にchとして
		ret.append(int(ch)) # retの末尾にchの表す整数を追加
	return ret # retを返す
def euler017_digit_count(n): # nを引数とする関数euler017_digit_countを定義
	c = 1 # cに1を代入
	while int(n / 10) > 0: # nを10で割った整数部分が0より大きい間
		n /= 10 # nを10で割る
		c += 1 # cに1を足す
	return c # cを返す
def euler017_ones_to_string(n): # nを引数とする関数euler017_ones_to_stringを定義
	return word[n % 10] # wordのn%10番目を返す
def euler017_is_equal(a, b): # aとbを引数とする関数euler017_is_equalの定義
	return a == b # aとbが等しければTrue、そうでなければFalseを返す
def euler017_divid_integer_part(a, b): # aとbを引数とする関数euler-17_divid_inateger_partを定義
	return int(a / b) # aをbで割った整数部分を返す
def euler017_string_length(s): # sを引数とする関数euler017_string_lengthの定義
	c = 0 # cに0を代入
	for ch in s: # s内の各要素をchとして
		c += 1 # cに1を足す
	return c # cを返す
def euler017_string_length_a(s): # sを引数とする関数euler017_string_length_aを定義
	return len(s) # sの長さを返す
