from Projeto import database, app
from Projeto.models import Produto

with app.app_context():
    database.create_all()