
# --- tuple

lista = ['dyego', 'maykon', 'rauen','granemann']
tupla = ('dyego', 'maykon', 'rauen','granemann')
print(tupla)

print(tupla[2])
print(lista[2])

lista[2] = 'Marchi' 

# A tupla não pode ser alterada
#tupla[2] = 'Marchi' 

print(lista)
print(tupla)

lista2 = list(tupla)
lista2[1] = 'Assunção'
print(lista2)