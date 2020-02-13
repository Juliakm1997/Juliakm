lista = []
tupla = ()
dicionario = { 'nome':'Maykon', 'sobrenome':'Granemann', 'idade':19 }
#print(dicionario['idade'])

pessoa1 = { 'nome':'Maykon', 'sobrenome':'Granemann' ,'idade':19, 'cpf':1535366977 }
pessoa2 = { 'nome':'Joao', 'sobrenome':'DasCoves', 'idade':20, 'cpf':4444444444 }
pessoa3 = { 'nome':'Tonho', 'sobrenome':'DoCorcel', 'idade':52, 'cpf':789534865321 }
pessoa4 = { 'nome':'Jose', 'sobrenome':'DoInformatica', 'idade':54, 'cpf':77777777 }

lista_pessoas = []
lista_pessoas.append(pessoa1)
lista_pessoas.append(pessoa2)
lista_pessoas.append(pessoa3)
lista_pessoas.append(pessoa4)
for p in lista_pessoas:
    print(p['sobrenome']) 


