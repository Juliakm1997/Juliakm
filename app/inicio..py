#-------- CTRL + K + C (comentar)
#-------- CTRL +K + U
#---- Imprimir info na tela
#---- Pular linha
print('\n')
# #---- Multiplicação de caractere
print('*'*50)
print('Olá, Usuário!')
print('Olá Júlia!')
print('\n')

#---- Pegar entrada do usuário
nome = input('Digite seu nome:')
sobrenome = input('Digite seu sobrenome:')

#---- Usando a função "format" para concatenação de string
print('Olá, {} {}'.format(nome, sobrenome))

---- Interpolação de strings
print(f'Olá, {nome} {sobrenome}')

idade = int (input('Digite a idade:'))
print(idade)


