from flask import Flask, render_template,redirect, url_for
from Projeto import app,database
from Projeto.forms import FormProduto
from Projeto.models import Produto

#Rota inicial do sistema
@app.route("/")
def index():
    produtos = Produto.query.order_by(Produto.valor_produto).all()
    return render_template("index.html",produtos = produtos)


#Rota de cadastro de produtos
@app.route("/cadastrar",methods = ["GET","POST"])
def cadastrar():

    #Trazer formulario
    form = FormProduto()

    #Condicional para validar o formulario
    if form.validate_on_submit():

        #Puxar valores recebidos pelo usuario
        produto = Produto(nome_produto = form.nome_produto.data,
                          descricao_produto = form.descricao_produto.data,
                          valor_produto = form.valor_produto.data,
                          disponivel_venda = form.disponivel_venda.data)

        #Adicionar no BD
        database.session.add(produto)

        #Comitar
        database.session.commit()

        #Redirecionar para pagina de listagem
        return redirect(url_for('index'))
    #Caso não ocorra, manter na página de cadastro
    return render_template("cadastrar.html",form=form)