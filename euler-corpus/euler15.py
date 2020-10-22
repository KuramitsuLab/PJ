def euler015(): # 関数euler015の定義
	facts = [1] * 21 # factsを21個の1からなるリストとする
	for i in range(20): # 20未満の非負整数を小さい方から順にiとして
		facts[i + 1] = facts[i] * (i + 1) # factsのi+1番目にfactsのi番目とi+1の積を代入
	dinomials = [0] * 21 # dinominalsを0が21個並んだリストとする
	for i in range(21): # 21未満の非負整数を小さい方から順にiとして
		dinomials[i] = int(facts[20] / (facts[i] * facts[20 - i])) # factsの20番目の要素をi番目の要素と20-i番目の要素の積で割った結果をdinominalsのi番目に格納する
	for i in range(20): # 20未満の非負整数iを小さい方から順に調べる
		for j in range(20): # 20未満の非負整数jを小さい方から順に調べる
			dinomials[j] += dinomials[j + 1] # dinominalsのj番目にj+1番目の要素を足す
	return dinomials[0] # dinominalsの最初の要素を返す
def euler015_combination(n, r): # nとrを引数とする関数euler015_combinationの定義
	facts = [1] * (n + 1) # factsを1がn+1個並んだリストとする
	for x in range(n): # n未満の非負整数nを小さい方から順に
		facts[x + 1] = facts[x] * (x + 1) # factsのx+1番目の要素にx番目の要素とx+1の積を代入
	return int(facts[n] / (facts[r] * facts[n - r])) # factsのn番目の要素をr番目とn-r番目の要素の積で割った結果を返す
def euler015_all_factorials(n): # nを引数とする関数euler015_all_factorialsの定義
	facts = [1] * (n + 1) # factsに1がn+1個繋がったリストを格納
	for x in range(n): # n未満の非負整数xを小さい方から順に
		facts[x + 1] = facts[x] * (x + 1) # factsのx+1番目の要素にx番目の要素とx+1積を代入する
	return facts # factsを返す
def euler015_pascal_triangle(n): # nを引数とする関数euler015_pascal_triangleの定義
	if n == 1: # もしnが1と等しければ
		return [1] # 1のみからなるリストを返す
	else: # そうでなければ
		l = euler015_pascal_triangle(n - 1) # euler015_pascal_triangleにn-1を渡した結果をlとする
		ret = [l[0], l[-1]] # retをlの最初の要素と末尾の要素からなるリストとする
		for i in range(n - 2): # n-2未満の非負整数iを小さい方から順に調べる
			ret.insert(i + 1, l[i] + l[i + 1]) # retのi+1番目にlのi番目とi+1番目の要素の和を追加する
		return ret # retを返す
