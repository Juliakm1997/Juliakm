# Cadastro do cliente
#---Função

def cadastro():
    nome= input ('nome:')
    sobrenome = input ('sobrenome:')
    telefone = input ('telefone:')
    cliente = {'nome': nome, 'sobrenome': sobrenome, 'tel': telefone}
    return cliente

def imprimir(cliente):
    print(f'{cliente['nome']};{clinete['sobrenome']};{cliente['telefone']}')

    
    # ou 
    # print(cliente)

c = cadastro()    
imprimir(c)