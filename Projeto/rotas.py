from flask import Flask, render_template,redirect
from Projeto import app,database
from Projeto.forms import FormProduto
from Projeto.models import Produto

@app.route("/")
def index():
    produtos = Produto.query.all()
    return render_template("index.html",produtos = produtos)

@app.route("/cadastrar",methods = ["GET","POST"])
def cadastrar():
    form = FormProduto()
    if form.validate_on_submit():
        produto = Produto(nome_produto = form.nome_produto,
                          descricao_produto = form.descricao_produto,
                          valor_produto = form.valor_produto,
                          disponivel_venda = form.disponivel_venda)
        database.session.add(produto)
        database.commit()
        return render_template("cadastrar.html",form=form)
    #return ("ghghhgfdgd")