# operazioni con le liste
l1=[1,2,3]
l2=[4,5,6]
print('l1:',l1)
print('l2:',l2)
# somma
print('l1+l2:',l1+l2)
# moltiplicazione
print('l1*5:',l1*5)

print('-'*30)

# operazioni con i set
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print('s1:',s1)
print('s2:',s2)
# differenza
print('s1-s2:',s1-s2)
print('s2-s1:',s2-s1)

print('-'*30)

# sfruttare set per eliminare duplicati dalle liste
L1 = [1,2,3,4,2]
print('L1 iniziale:', L1)
S1 = set(L1)
L1 = list(S1)
print('L1 finale:', L1)

# sfruttare liste per cambiare un carattere di una stringa
s1 = 'stringa'
print('s1 iniziale:', s1)
l1=list(s1)
l1[3]=str(l1[3]).upper()
print('s1 finale:', ''.join(l1))


