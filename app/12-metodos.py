# cadastro de cliente
def cadastro():
    nome = input('nome: ')
    sobrenome = input('sobrenome: ')
    telefone = input('telefone: ')
    cliente = {'nome':nome, 'sobrenome':sobrenome, 'tel':telefone}
    return cliente

def imprimir(cliente):
    print( f"{cliente['nome'] };  {cliente['sobrenome']}, {cliente['tel']}" )

c = cadastro()
imprimir(c)