from flask import Flask, render_template

#Criar rota
## Rota 1
nome= 'Site Flask'
lista_empresas = ['Proway', 'HBSIS', 'TSystems', 'Senior', 'Philips']

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', titulo= nome)


## Rota 2
@app.route('/empresa')
def cadastro():
    return render_template('empresa.html', titulo= nome, empresas=lista_empresas)


app.run(debug=True)
