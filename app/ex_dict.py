#-----CRIANDO CADASTRO

cervejas = {'marca':'skol', 'tipo':'pilsen'}
cervas = {}

# --- Cadastro de cerveja  
marca= input ('Digite o marca da cerveja:')
tipo= input ('Digite o tipo da cerveja:')

cervas['marca'] = marca
cervas['tipo'] = tipo

print(cervas)

#---Cadastro de pessoa
#--Criando um dicionário vazio
cadastro = {}

nome= input ("Digite o nome:")
sobrenome= input ('Digite o sobrenome:')
cpf= input ('Digite o cpf:')

# #--Criando as chaves/valores após a criação do dicionário
cadastro['nome']=nome
cadastro['sobrenome']=sobrenome
cadastro['cpf']=cpf

print(cadastro)

#----Criando o dicionário com as chaves e valores
nome= input ("Digite o nome:")
sobrenome= input ('Digite o sobrenome:')
cpf= int(input ('Digite o cpf:'))

cadastro2 = {'nome':nome, 'sobrenome':sobrenome, 'cpf':cpf}

print(cadastro2)

##################################################################
