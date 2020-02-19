# ----- Classes -----
# Metodo construtor

class Calculadora:
    n1 = 0
    n2 = 0
    resultado = 0

    # Criação de um método construtor, com parêmetros
    def __init__(self, numero1, numero2):
        self.n1 = numero1
        self.n2 = numero2

    # método soma utiliza as variáveis da classe n1 e n2 para realizar a soma
    # o resultado da soma é armazenado na variável da classe 'resultado'
    def soma(self):
        self.resultado = self.n1 + self.n2

# Instanciando um objeto da classe Calculadora passando dois argumentos
# Os dois argumentos passados durante o instancimendo, são passados para o metodo init(Construtor)
calc = Calculadora(10, 20)
# Chamada do método  'soma' da classe 'Calculadora'
calc.soma()
# impressao do valor da variável 'resultado' da classe 'Calculadora'
print(calc.resultado)
