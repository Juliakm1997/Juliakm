# Ler os dados do arquivo criado na atividade 3
# Tratar cada linha do arquivo para remover os caracteres especiais '\n' ou espaços em branco
# Mostrar os dados formando com f-strings

def salvar(dado):
    arquivo =  open(r'12-02\Exercicios\usuario.txt', 'a')
    arquivo.write(f'  {dado}\n')
    arquivo.close()
    return 'Dado salvo com sucesso!'

def ler():
    lista=[]
    arquivo = open(r'12-02\Exercicios\usuario.txt', 'r' ) 
    for linha in arquivo:  
        linha_tratada = linha.strip()
        vetor = linha_tratada.split(';')
        dado_formatado = f"Nome: {vetor[0]}"
        lista.append(dado_formatado)
    return lista
      
usuario = input('Digite o nome: ') 
msg = salvar(usuario)
print(msg)
lista = ler()
print(lista[0])



