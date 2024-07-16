from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///produtos.db"
app.config["SECRET_KEY"] = "4b6dceed7214c6316c75b11878760285"

database = SQLAlchemy(app)

from Projeto import rotas
