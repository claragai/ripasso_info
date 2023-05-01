# apertura in lettura, python restituisce un errore se non trova il file
f = open('prova.txt','r',encoding='utf-8')

# lettura file per carattere
print('**lettura per carattere**')

s = f.read(1)
print(s)
while s:
    s = f.read(1)
    print(s)
f.close()
print()

# lettura file due caratteri per volta
print('**lettura 2 caratteri**')
f = open('prova.txt','r',encoding='utf-8')
s = f.read(2)
print(s)
while s:
    s = f.read(2)
    print(s)
f.close()
print()

# lettura intero file
print('**lettura intero file**')
f = open('prova.txt','r',encoding='utf-8')
s = f.read()
print(s)
f.close()
print()

# lettura file per righe
print('**lettura per righe**')
f = open('prova.txt','r',encoding='utf-8')
for line in f:
    print(line[:-1])
f.close()
print()

# lettura file per righe
print('**lettura per righe**')
f = open('prova.txt','r',encoding='utf-8')
line = f.readline().rstrip('\n')
print(line)
while line:
    line = f.readline().rstrip('\n')
    print(line)
f.close()
print()

# lettura file per righe con with
print('**lettura per righe**')
with open('prova.txt',"r") as f:
    for line in f:
        print(line[:-1])
