# Criar uma classe pessoa
# Recebe os seguintes dados no construtor da classe:
#   Nome, Sobrenome, Idade, Sexo
# Armazene os dados em variáveis privadas
# Crie os metodos Get e Set para cada variavel
# Crie um objeto da classe
# altera o nome pelo metodo set
# exiba o novo nome pelo metodo get


class Pessoa:
    def __init__(self, nome, sobrenome, idade, sexo):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        self.__sexo = sexo

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
       self.__nome = nome  
          

    def get_sobrenome(self):
        return self.__sobrenome

    def set_sobrenome(self, sobrenome):
       self.__sobrenome = sobrenome  


    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
       self.__idade = idade 



    def get_sexo(self):
        return self.__sexo        

    def set_sexo(self, sexo):
        self.__sexo = sexo


pessoa = Pessoa('Júlia', 'Marchi', 22, 'F')
pessoa.set_nome('Lara')

print(f"Nome: {pessoa()}")
print(f"Novo Nome: {pessoa.get_nome()}") 