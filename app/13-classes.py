#classes

class Pessoa:
    nome = ''
    sobrenome = ''

    def imprimir(self):
        print(f'{self.nome};{self.sobrenome}')


p1 = Pessoa()
p1.nome = input('Nome:')
p1.sobrenome = input('Sobrenome:')
p1.imprimir()




