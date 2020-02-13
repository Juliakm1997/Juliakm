
def dirige(nome):
    print(f'O {nome} pode dirigir')

def carona(nome):
    print(f'O {nome} so pode ir de carona')

nome = 'Maykon'
idade = 17

if idade >=18:
    dirige(nome)
else:
    carona(nome)