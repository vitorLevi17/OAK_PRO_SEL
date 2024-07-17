from Projeto import database

#A classe produto vira uma entidade no BD
class Produto(database.Model):
    # Campo numerico, auto_incrementado que armazena o id produto
    id = database.Column(database.Integer, primary_key = True)

    # Campo de texto que armazena o nome do produto
    nome_produto = database.Column(database.String, nullable = False, unique = True)

    # Campo de texto que armazena a descrição do produto
    descricao_produto = database.Column(database.String)

    #Campo numerico que armazena o valor do produto
    valor_produto = database.Column(database.Float,nullable = False)

    # Campo booleano para receber a disponibilidade do produto
    disponivel_venda = database.Column(database.Boolean, default = True, nullable = False)
