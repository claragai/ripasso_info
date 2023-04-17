l = [1, 4, 3, 0, 1]

if False:
	#operatore 'in' per fare ricerche all'interno della lista
	b = 2 in l
	print('type', type(b))
	print('bool', b)

if False:
	#operatore 'del' per eliminare elementi della lista
	del l[2]
	print(l)


if False:
	#metodo pop per eliminare elementi della lista e ritornarli
	print('elemento rimosso', l.pop(1))
	print(l)

if False:
	#metodo 'sort' ordina una lista
	l = [8, 2, 0, 4, 6]
	l.sort()
	print('lista ordinata', l)

if False:
	#funzione 'sorted' ritorna la lista ordinata
	l = [8, 2, 0, 4, 6]
	print('lista ordinata', sorted(l))
	print('lista non modificata', l)

if False:
	#cicla su una lista usando l'indice
	for i in range(len(l)):
	    print('index:',i)
	    print('element:',l[i])

if False:
	#cicla su una lista usando gli elementi 
	for el in l:
	    print('element:',el)

if False:
	#cicla su una lista usando indici e elementi 
	for (i,el) in enumerate(l):
	    print('index:',i)
	    print('element:',el)
