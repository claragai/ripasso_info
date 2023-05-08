x = 5
y = 6
print('x =',x)
print('y =',y)

# definizione funzione per la somma
def somma(a,b):
    res= a+b
    a = 100
    print('x dentro la funzione ' + str(a))
    return res

print('x fuori la funzione '+str(x))
s = somma(x,y)
print('somma =', s)
print('x fuori la funzione '+str(x))

print('-' * 30)
# definizione funzione per la somma e media
def somma_media(a,b):
    res_s = a+b
    res_m = (a+b)/2
    return res_s,res_m

s,m = somma_media(x,y)
print('somma =', s)
print('media =', m)


print('-' * 30)

x = [5,8,9]
y = [6]
print('x =',x)
print('y =',y)

# definizione funzione per sommare elementi di due liste
def somma_elementi_liste(a,b):
	res = 0
	for el in a:
		res += el
	for el in b:
		res += el
	a[0] = 0
	print('x dentro la funzione' + str(a))
	return res

print('x fuori la funzione' + str(x))
print('somma elementi:', somma_elementi_liste(x,y))
print('x fuori la funzione' + str(x))

