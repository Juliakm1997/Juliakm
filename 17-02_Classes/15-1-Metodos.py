# Métodos ---
# Argumentos ordenados
# Argumentos nomeados
# Argumentos opcionais

# Métodos
# Exemplo de argumentos ordenados
def soma(numero1, numero2, numero3):
    resultado = numero1 + numero2 + numero3
    return resultado

# São passados os valores na ordem em que estão declarados no método
res = soma(10, 20, 30)
print(res)

# Criação de método para uso de argumentos nomeados
def subtracao(n1, n2, n3):
    resultado = n1 - n2 - n3
    return resultado
# Chamada de métodos passando argumentos nomeados
# Os argumentos são passados de acordo com o nome e não mais por posição
res2 = subtracao( n2=40, n1=20 , n3=5)
print(res2)

# Criação de método para uso de argumentos opcionais
def multiplicacao(n1, n2, n3=1):
    resultado = n1 * n2 * n3
    return resultado

# Exemplo de uso de argumento opcional, onde eu posso passar o ultimo argumento ou não
# Caso o ultimo argumento não seja passado ele assumirá o valor default = 1
res3 = multiplicacao(5, 2)
print(res3)