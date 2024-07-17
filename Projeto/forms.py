from flask_wtf import FlaskForm
from wtforms import StringField,FloatField,BooleanField, SubmitField,FileField

from wtforms.validators import DataRequired,EqualTo,Length, ValidationError
from Projeto.models import Produto

class FormProduto(FlaskForm):
    nome_produto = StringField("Nome do produto",validators=[DataRequired()])
    descricao_produto = StringField("Descrição",validators=[DataRequired()])
    valor_produto = FloatField("Preço",validators=[DataRequired()])
    disponivel_venda = BooleanField("Disponível para venda")
    submit = SubmitField("Cadastrar")



