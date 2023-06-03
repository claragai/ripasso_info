# definizione di due set
s1 = {1, 2, 3}
s2 = {2, 3, 4}

# scorrere il set (non è possibile farlo per indice)
for n in s1:
    print(n)

print('s1:', s1)
print('s2:', s2)
# esempi metodi e operazioni utili con i set
print('intersezione S1 e S2:', s1.intersection(s2))
print('differenza S1 e S2:', s1 - s2)
print('differenza S2 e S1:', s2 - s1)
