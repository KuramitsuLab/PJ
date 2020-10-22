def euler011(): # 関数euler001の定義
	grid = """""".split() # gridに文字列を空白文字で分割したリストを代入
	q = [] # qに空リストを代入
	for ch in grid: # grid中の各要素を順にchとして
		q.append(int(ch)) # qの末尾にchの表す数値を追加
	m = 0 # mを0にする
	for i in range(20): # 0から20未満の整数を順にiとして
		for j in range(20): # 0から20未満の整数を順にjとして
			if j <= 16: # もしjが16以下であれば
				m = max(m, q[i*20+j] * q[i*20+j+1] * q[i*20+j+2] * q[i*20+j+3]) # 現在のmと(q[i*20+j] * q[i*20+j+1] * q[i*20+j+2] * q[i*20+j+3])のうち大きい方を新しいmとする
				if i <= 16: # もしiが16以下であれば
					m = max(m, q[i*20+j] * q[(i+1)*20+j+1] * q[(i+2)*20+j+2] * q[(i+3)*20+j+3]) # 現在のmと(q[i*20+j] * q[(i+1)*20+j+1] * q[(i+2)*20+j+2] * q[(i+3)*20+j+3])のうち大きい方を新しいmとする
			if 4 <= j and i <= 16: # もしjが4以上でiが16以下であれば
				m = max(m, q[i*20+j] * q[(i+1)*20+j-1] * q[(i+2)*20+j-2] * q[(i+3)*20+j-3]) # 現在のmと(q[i*20+j] * q[(i+1)*20+j-1] * q[(i+2)*20+j-2] * q[(i+3)*20+j-3])のうち大きい方を新しいmとする
			if i <= 16: # もしiが16以下であれば
				m = max(m, q[i*20+j] * q[(i+1)*20+j] * q[(i+2)*20+j] * q[(i+3)*20+j]) # 現在のmと(q[i*20+j] * q[(i+1)*20+j] * q[(i+2)*20+j] * q[(i+3)*20+j])のうち大きい方を新しいmとする
	return m # mを返す
def euler011_less_or_equal(a, b): # aとbを引数とする関数euler011_less_or_equalの定義
	return a <= b # aがb以下であればTrue、そうでなければFalseを返す
def euler011_less_or_equal_a(a, b): # aとbを引数とする関数euler011_less_or_equal_aの定義
	res = b - a # resにbとaの差を代入
	return res >= 0 # resが0以上であればTrue、そうでなければFalseを返す
def euler011_over_or_equal(a, b): # aとbを引数とする関数euler011_over_or_equalの定義
	return b <= a # bがa以下であればTrue、そうでなければFalseを返す
def euler011_over_or_equal_a(a, b): # aとbを引数とする関数euler011_ver_or_equal_aの定義
	res = b - a # resにbとaの差を代入
	return res <= 0 # resが0以下であればTrue、そうでなければFalseを返す
def euler011_string_space_split(s): # sを引数とする関数euler011_string_space_splitの定義
	sl = [] # slに空リストを代入
	buf = "" # bufに空文字列を代入
	for ch in s: # s内の全ての要素を順にchとして
		if ch == " ": # もしchが半角スペースなら
			sl.append(buf) # slの末尾にbufを追加
			buf = "" # bufを空文字列にする
		else: # そうでなければ
			buf += ch # bufにchを加える
	sl.append(buf) # slの末尾にbufを追加
	return sl # slを返す
def euler011_zero_to_n_list(n): # nを引数とする関数euler011_zero_to_n_listの定義
	ret = [] # retに空リストを代入
	a = 0 # aに0を代入
	while a < n: # aがn未満の間
		ret.append(a) # retの末尾にaを追加
		a += 1 # aに1を足す
	return ret # retを返す
def euler011_zero_to_n_list_a(n): # nを引数とする関数euler011_zero_to_n_list_aの定義
	return list(range(n)) # 0からn-1までを順に要素として持つリストを返す
def euler011_upward_point(x, y): # x,yを引数とする関数euler011_upward_pointの定義
	return (x, y - 1) # xとy-1の組を返す
def euler011_downward_point(x, y): # x,yを引数とする関数euler011_downward_pointの定義
	return (x, y + 1) # xとy+1の組を返す
def euler011_left_point(x, y): # x,yを引数とする関数euler011_left_pointの定義
	return (x - 1, y) # x-1とyの組を返す
def euler011_right_point(x, y): # x,yを引数とする関数euler011_right_pointの定義
	return (x + 1, y) # x+1とyの組を返す
def euler011_upper_left_point(x, y): # x,yを引数とする関数euler011_upper_left_pointの定義
	return (x - 1, y - 1) # x-1とy-1の組を返す
def euler011_upper_right_point(x, y): # x,yを引数とする関数euler011_upper_right_pointの定義
	return (x + 1, y - 1) # x+1とy-1の組を返す
def euler011_lower_left_point(x, y): # x,yを引数とする関数euler011_lower_left_pointの定義
	return (x - 1, y + 1) # x-1とy+1の組を返す
def euler011_lower_right_point(x, y): # x,yを引数とする関数euler011_lower_right_pointの定義
	return (x + 1, y + 1) # x+1とy+1の組を返す
