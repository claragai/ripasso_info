"""
Per avere la documetazione completa sulla formattazione lanciare sulla console il comando "help('FORMATTING')"

    format_spec     ::= [[fill]align][sign][#][0][width][grouping_option][.precision][type]
    fill            ::= <any character>
    align           ::= "<" | ">" | "=" | "^"
    sign            ::= "+" | "-" | " "
    width           ::= digit+
    grouping_option ::= "_" | ","
    precision       ::= digit+
    type            ::= "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
"""

s = 'ciao'

# allineamento a destra
# print(format(s, '>10'))
print(f"stringa: {s:>10}")

# allineamento al centro
# print(format(s, '^10'))
print(f"stringa: {s:^10}")

# allineamento al centro con riempimento
# print(format(s, '-^10'))
print(f"stringa: {s:-^10}")

print('-' * 30)

f = 103.12313213213211
# formattazione numero float allineato al centro
# prima cifra: numero totale caratteri occupati
# seconda cifra: numero cifre significative
print(f"numero: {f:^10.5}")

# formati per numeri float: e, E (esponenziale)
# formattazione numero esponenziale allineato al centro
print(f"numero: {f:^10.5e}")

print('-' * 30)

# formati per numeri int : b (binario), h, H (esadecimale), o (ottale),
d = -103
print(f"numero: {d:08b}")

print('-' * 30)

# conversione binario (stringa) a decimale
b = '1010101'
n = int(b,2)
print('numero:', n)

# conversione esadecimale (stringa) a decimale
h = 'a1f056'
n = int(h, 16)
print('numero:', n)

# conversione binario/esadecimale (int) a decimale
print('numero:', 0b1010101)
print('numero:', 0xa1f056)

