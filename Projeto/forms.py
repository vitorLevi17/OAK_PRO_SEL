from flask_wtf import FlaskForm
from wtforms import StringField,FloatField,BooleanField, SubmitField
from wtforms.validators import DataRequired


class FormProduto(FlaskForm):
    # Campo de texto que recebe o nome do produto
    nome_produto = StringField("Nome do produto",validators=[DataRequired()])

    # Campo de texto que recebe a descrição do produto
    descricao_produto = StringField("Descrição",validators=[DataRequired()])

    # Campo numerico que recebe o valor do produto
    valor_produto = FloatField("Preço",validators=[DataRequired()])

    # Campo booleano para receber a disponibilidade do produto
    disponivel_venda = BooleanField("Disponível para venda")

    # Botão para cadastrar o produto
    submit = SubmitField("Cadastrar")



