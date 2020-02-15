from flask import Flask, render_template, request, redirect

from empresa import Empresa

#Criar rota
## Rota 1
nome= 'Site Flask'

lista_empresas = []

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', titulo= nome)


## Rota 2
@app.route('/empresa')
def cadastro():
    return render_template('empresa.html', titulo= nome, empresas=lista_empresas)

##Nova Rota
@app.route('/cadastro-empresa')
def cadastro_empresa():
    return render_template('cadastro-empresa.html', titulo=nome)

@app.route('/salvar-empresa')
def salvar_empresa():
    #--Objeto da classe
    empresa = Empresa()
    #------------------
    empresa.nome = request.args['nome']
    empresa.email = request.args['email']
    empresa.email = f"{empresa.email}@hbsis.com.br"
    lista_empresas.append(empresa)
    return redirect('/empresa') 



#---- Executa o servidor flask e inicia a app
#--- Parâmetro debug=True, 
#   faz servidor reiniciar quando arquivo python for alterado

app.run(debug=True)
