from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Inicia a aplicação
app = Flask(__name__)

#Configuração do BD
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///produtos.db"

#CHAVE SECRETA DA APLICAÇÃO
app.config["SECRET_KEY"] = "4b6dceed7214c6316c75b11878760285"

# Inicializa a extensão SQLAlchemy com a aplicação Flask
database = SQLAlchemy(app)

from Projeto import rotas
