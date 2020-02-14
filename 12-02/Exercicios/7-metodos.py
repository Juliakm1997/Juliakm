# Criar um método que recebe dos numeros inteiros
# Metodos calcula a soma dos dois números e armazena em uma variável
# Metodo retorna a variavel com o resultado
# Imprimir o retorno do método



def calcular(n1, n2):
    soma = n1 + n2
    return soma  


numero1= int(input('Digite o primeiro número: '))
numero2= int(input('Digite o segundo número: '))

soma = calcular(numero1, numero1)
print(f'Soma= {soma}')