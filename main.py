from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#funcionalidade de enviar mensagem:
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# Criar 1ª página = 1ª rota:
@app.route("/")
def homepage():
    return render_template("index.html")

# Roda o aplivativo:
socketio.run(app, host="172.25.128.1")

# Websocket -> tunel
