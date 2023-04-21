N = 4 # numero righe
M = 5 # numero colonne

t = []
if False:
	# creare una tabella (matrice NxM) con tutti zero
	for i in range(N):
		t.append([])
		for j in range(M):
			t[i].append(0)

if True:
	# creare una tabella (matrice NxM):
	#  0  1  2  3 ..
	# 10 11 12 13 .. 
	# .. .. .. .. ..
	# 40 41 42 43 ..
	# .. .. .. .. ..

	for i in range(N):
		t.append([])
		for j in range(M):
			t[i].append(10*i + j)

if True:
	# stampa t per come lo vede python
	print(t)
	print()

	# stampa t (stampa una riga poi va a capo)
	for i in range(N):
		for j in range(M):
			print(t[i][j], '', end='')
		print()
	print()

	# stampa t (stampa una riga poi va a capo) 
	for riga in t:
		for el in riga:
			print(el, '', end='')
		print()
	print()

if True:
	# stampa trasposta t (stampa una colonna poi va a capo)
	for j in range(M):
		for i in range(N):
			print(t[i][j], '', end='')
		print()
	print()
