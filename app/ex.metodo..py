# Método 1 - Cadastra uma cerveja: nome, tipo
# Método 2 - Armazenar em um arquivo texto 
# Método 3 - ler os dados armazenados no arquivo texto

## Cadastro
def cadastrar()
    cerveja = {}

    nome= input('Digite o nome da cerveja:')
    tipo= input('Digite o tipo da cerjeva:')

    cerveja['nome']= nome
    cerveja['tipo']=tipo

# print(f'nome:{nome} ; tipo:{tipo}')

## Armazenar em um arquivo texto

def salvar(dado)
    arquivo =  open(r'app\cerveja.txt', 'a')
    arquivo.write(f'{dado}\n')
    arquivo.close()
    return 'Dado salvo no arquivo'

## Ler dados armazenados
def ler()
    lista = []
    arquivo =  open(r'app\cerveja.txt', 'r')
    for linha in arquivo:
        linha_tratada = linha.strip()
        vetor = linha_tratada.strip(';')
        lista.append(linha)
    return lista


c = cadastrar()    