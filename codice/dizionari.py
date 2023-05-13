from operator import itemgetter

# creare un dizionario
d = {'a': 2,'r': 1,'w': 4,'y': 0,'b': 2}

# accedere a un elemento (restituisce errore se la chiave non è presente)
print('corrispondenza chiave a:', d['a'])

# controllare se una chiave è presente 
print('è presente la chiave a?:', 'a' in d)
print('è presente la chiave t?:', 't' in d)

# cambiare o aggiungere un elemento
d['w'] = 5
d['z'] = 3

print(d)

# ciclare sul dizionario per chiavi
for key in d:
	print('chiave:', key, 'valore:', d[key])

print()
print('-' * 30)

# ciclare sul dizionario per chiavi e valori
for key,value in d.items():
	print('chiave:', key, 'valore:', value)

print()
print('-' * 30)

# ciclare sul dizionario per chiavi ordinate
for key in sorted(d):
	print('chiave:', key, 'valore:', d[key])

print()
print('-' * 30)

# ciclare sul dizionario per chiavi ordinate
for key,value in sorted(d.items(), key=itemgetter(1)):
	print('chiave:', key, 'valore:', value)
