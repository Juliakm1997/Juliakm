# Criar o cadastro de bebidas
# Solicitar o nome através do console e armazenar em uma variável
# Solicitar o teor alcoolico através do console e armazenar em uma variável
# Cria um dicionário com os dados lidos
# Imprimir o dicionário formatando os dados através de f-strings



cadastro = {}
cadastro['nome'] = input('Digite o nome : ')
cadastro['alcoolismo'] = float(input('Digite o teor alcoolico: '))


print(f"Nome: {cadastro['nome' ]}\nTeor ALcoolico: {cadastro['alcoolismo']}")