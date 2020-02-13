#metodo para fechamento automatico do arquivo
with open('pessoa.txt', 'a') as arquivo:
    arquivo.write(f'  {nome};{sobrenome}\n')