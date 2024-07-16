from Projeto import database
class Produto(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    nome_produto = database.Column(database.String, nullable = False, unique = True)
    descricao_produto = database.Column(database.String)
    valor_produto = database.Column(database.Float,nullable = False)
    disponivel_venda = database.Column(database.Boolean, default = True, nullable = False)
