# uso eccezioni per gestire errori generati dalle funzioni built-in di Python
try:
    # f = open('nonesiste.txt','r') # solleva un'eccezione 'FileNotFoundError'
    a = 's' + 4 # solleva un'eccezione 'TypeError'
    # a = 10
    print('a =',a)
except TypeError as message: # sfrutta il messagio generato in automatico durante la costruzione dell'eccezione
    print('ERR:', str(message))
except FileNotFoundError:
    print('eccezione trovata file')
finally: # blocco eseguito in entrambi i casi
    print('fine programma')

# costruzione di un'eccezione
try:
    a = -4
    if a < 0:
        raise ValueError("valore negativo non permesso (" + str(a) + ")")
    # a = 10
    print('a =',a)
except TypeError as m:
    print('Err:', m)
finally:
    print('fine programma')
