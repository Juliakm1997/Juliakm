# Classes
# Variáveis de classe
# Métodos de classe
# self

class Calculadora:
    n1 = 0
    n2 = 0

    def soma(self):
        resultado = self.n1 + self.n2
        return resultado

    def subtracao(self):
        resultado = self.n1 - self.n2
        return resultado

    def multiplicacao(self):
        resultado = self.n1 * self.n2
        return resultado

    def divisao(self):
        resultado = self.n1 / self.n2
        return resultado

# Criação de uma variavél de tipo Classe Calculadora
# Em POO = Instanciando um objeto da classe Calculadora
calculadora =  Calculadora()

calculadora.n1 = 10
calculadora.n2 = 20

res = calculadora.soma()
res2 = calculadora.subtracao()
res3 = calculadora.multiplicacao()
res4 = calculadora.divisao()
print(res)
print(res2)
print(res3)
print(res4)

