from flask_mysqldb import MySQLdb

# A conexão e cursor serão sempre os mesmos
class PessoaDao:
    def__init__(self)
    self.__conexao = MySQLdb.connect
conexao = MySQLdb.connect(host="mysql.topskills.study", database= "topskills01", user= "topskills01", passwd= "ts2019")

    self.__cursor = self.__conexao.cursor()


def lista_todos():
    lista = []
    self.__cursor.execute("SELECT*FROM 01_PN_PESSOA")
    for p in self.__cursor.fetchall():
    # print (p) - selecionar toda a tabela
    # print (p[1]) - selecionar uma coluna especifica
        print(f'id: {p[0]} nome: {p[1]} sobrenome: {p[2]} idade: {p[3]} sexo:{p[4]} ')

def buscar_por_id(self, id):
    self.__cursor.execute(f"SELECT*FROM 01_PN_PESSOA WHERE ID = {id}")   
    p = self.__cursor.fetchone()
    print(f'id: {p[0]} nome: {p[1]} sobrenome: {p[2]} idade: {p[3]} sexo:{p[4]} ')

def inserir(self, nome, sobrenome, idade, sexo):
    self.__cursor.execute(f"INSERT INTO 01_PN_PESSOA (NOME, SOBRENOME, IDADE, SEXO) VALUES ({nome} {sobrenome} {idade} {sexo})")    
    self.__conexao.commmit()

def alterar(self, nome, sobrenome, idade, sexo, id):
    self.__cursor.execute(f"UPDATE 01_PN_PESSOA SET NOME= '{nome}', SOBRENOME= '{sobrenome}', IDADE= {idade}, SEXO= '{sexo}'WHERE ID = [id]")

def deletar(self, id):
    self.__cursor.execute    





pd = PessoaDao
pd.listar_todos()     
print('_'*10)
pd.buscar_por_id(4)    



