# ----- Classes -----
# variáveis privadas
# getters e setters

class Calculadora:
    def __init__(self, numero1, numero2):
        # Criando variáveis privadas da classe
        # Variáveis privadas tem 2x '_' como precedente no nome
        self.__n1 = numero1
        self.__n2 = numero2
        self.__resultado = 0
        
    def soma(self):
        self.__resultado = self.__n1 + self.__n2

    def get_resultado(self):
        return self.__resultado

    def set_n1(self, valor):
        self.__n1 = valor

    def set_n2(self, valor):
        self.__n2 = valor

    def get_n1(self):
        return self.__n1

    def get_n2(self):
        return self.__n2

# Instanciando um objeto da classe Calculadora, passando argumentos para o construtor da classe
c = Calculadora(10 , 20)
# Tentando imprimir variáveis privadas
# Esta linha dará erro
print(c.__n1, c.__n2)

# Chamando um método get para recuperar o valor de uma variável privada
print(c.get_resultado())



