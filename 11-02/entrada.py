#---- Pegar entrada do usuário
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

#---- Usando a funcao format para concatenação de string
print('Ola {} {} '.format(nome, sobrenome) )

#---- Interpolação de strings
print( f'Ola {nome} {sobrenome}' )

#---- Conversao de String para Inteiro
idade = int( input('Digite a idade') )
#---- Ao imprimir
print(idade)
