from flask import Flask, render_template,redirect, url_for
from Projeto import app,database
from Projeto.forms import FormProduto
from Projeto.models import Produto

@app.route("/")
def index():
    produtos = Produto.query.order_by(Produto.valor_produto).all()
    return render_template("index.html",produtos = produtos)

@app.route("/cadastrar",methods = ["GET","POST"])
def cadastrar():
    form = FormProduto()
    if form.validate_on_submit():
        produto = Produto(nome_produto = form.nome_produto.data,
                          descricao_produto = form.descricao_produto.data,
                          valor_produto = form.valor_produto.data,
                          disponivel_venda = form.disponivel_venda.data)
        database.session.add(produto)
        database.session.commit()
        return redirect(url_for('index'))

    return render_template("cadastrar.html",form=form)