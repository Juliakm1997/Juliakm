dicionario2 = {'nome':'', 'sobrenome':'', 'idade': 0}
dicionario3 = {'nome':'Maykon', 'sobrenome':'Granemann', 'idade': 18 }


nome = input('Digite o nome: ')
idade = int(input('digite a sua idade: '))

dicionario = {}
dicionario['nome'] = nome
dicionario['idade'] = idade 

if idade >= 18:
    cerveja = input('digite a cerveja:')
    dicionario['cerveja']= cerveja
else:
    refrigerante = input('digite p refrigerante:')
    dicionario['refrigerante'] = refrigerante

print(dicionario)

