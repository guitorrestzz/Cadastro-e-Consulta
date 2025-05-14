from flask import Flask, render_template, redirect, request
from controllers.clientes import Cliente
from controllers.sql import Banco
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)

# Rotas
# ------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

# ------------------------------------------------------
@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        cliente = Cliente(request.form.get('nome'), request.form.get('email'), request.form.get('telefone'))
        try:
            cliente.inserir_dados()
            socketio.emit('atualizar_lista')
        except Exception:
            return render_template('erro.html', erro="impossível cadastrar")
    return render_template('cadastro.html')

# ------------------------------------------------------
@app.route('/consulta', methods=['POST', 'GET'])
def consulta():
    cliente = Cliente()
    return render_template('consulta.html', clientes=cliente.consultar_dados())

socketio.run(app, host="127.0.0.1", port=80, debug=True)
