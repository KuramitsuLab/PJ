def euler020(): # 関数euler020の定義
	fact = 1 # factに1を代入
	for i in range(100): # 100未満の非負整数を小さい方から順にiとして
		fact *= (i + 1) # factにi+1を掛ける
	s = str(fact) # sにfactの文字列表現を代入
	q = [] # qに空リストを代入
	for ch in s: # sの各要素を順にchとして
		q.append(int(ch)) # qの末尾ににchの表す整数を追加
	return sum(q) # qの全要素の総和を返す
def euler020_factorial(n): # nを引数とする関数euler020_factorialの定義
	ret = 1 # retに1を代入
	for x in range(n): # n未満の非負整数を小さい方から順にxとして
		ret *= (x + 1) # retにx+1を掛ける
	return ret # retを返す
def euler020_digit_sum(n): # nを引数とする関数euler020_digit_sumの定義
	q = str(n) # qにnの文字列表現を代入
	s = 0 # sに0を代入
	for x in q: # qの各要素を順にxとして
		s += int(x) # sにxの表す整数を足す
	return s # sを返す
