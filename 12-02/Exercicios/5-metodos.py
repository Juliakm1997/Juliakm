# Criar um metodo para ler o nome de uma pessoa
# Método retornar o nome lido
# Imprimir o retorno do metodo formando com f-strings

def ler():
    usuario = input('Digite o nome: ') 
    return usuario
      
usuario = ler()
print(f'Nome: {usuario}')
