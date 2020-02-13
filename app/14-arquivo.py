nome = 'Maykon'
sobrenome = 'Graneman'

arquivo =  open('pessoa.txt', 'a')
arquivo.write(f'  {nome};{sobrenome}\n')
arquivo.close()

arquivo =  open('pessoa.txt', 'r')
for l in arquivo:
    print( l.strip() )
arquivo.close()



## Metodo1 =  Cadastrar uma cerveja: nome, tipo
## Metodo2 = Armazenar em um arquivo texto
## Metodo3 = Ler os dados armazenados no arquivo texto