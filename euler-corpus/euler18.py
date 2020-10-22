def euler018(): # 関数euler018の定義
	for i in reversed(range(len(tri) - 1)): # triの長さ-1未満の非負整数を大きい方からiとして
		for j in range(len(tri[i])): # triのi番目の長さ未満の非負整数を小さい方からjとして
			tri[i][j] += max(tri[i + 1][j], tri[i + 1][j + 1]) # tri[i+1][j]とtri[i+1][j+1]の大きい方をtri[i][j]に足す
	return tri[0][0] # triの先頭要素の先頭要素を返す
