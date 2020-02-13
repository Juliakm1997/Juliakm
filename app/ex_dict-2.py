# diconario = {}
# dicionario2 = {'nome':'', 'sobrenome':'', 'idade':0}
# dicionario3 = {'nome':'Júlia', 'sobrenome':'Marchi', 'idade':22}

nome = input('Digite o nome:')
idade = int(input('Digite a idade:'))

dicionario = {}
dicionario['nome']=nome
dicionario['idade']=idade

if idade >=18:
    cerveja= input('Digite a cerveja:')
    dicionario['cerveja']=cerveja
else:
    bebidasalcool= input('Digite a bebida desejada')   
    dicionario['bebidasalcool'] = bebidasalcool

    print(dicionario)



