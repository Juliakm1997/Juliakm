#---- Criando variável do tipo Int a partir do input
idade = int( input('Digite a sua idade: ') )

#---- Instrução if e else e elif
if idade >= 18 :
    print('Maior de idade, pode beber')
elif idade < 14 :
    print('Menor de idade, nem guarana')
else:
    print('Menor de idade, so guarana')