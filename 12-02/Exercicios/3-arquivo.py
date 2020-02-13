# Solicitar o nome do usuário através do console
# Salvar o dado em uma variável
# Salvar a variavel em um arquivo texto


def salvar(dado):
    arquivo =  open(r'12-02\Exercicios\usuario.txt', 'a')
    arquivo.write(f'  {dado}\n')
    arquivo.close()
    return 'Dado salvo com sucesso!'

usuario = input('Digite o nome: ') 
print(salvar(usuario))
