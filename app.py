from flask import Flask, render_template, request, redirect, url_for, flash, session
from sqlalchemy import select
from models import Produto, db_session, Fornecedor, Categoria, Funcionario, Movimentacao, User
from functools import wraps
import plotly.express as px
import pandas as pd
from datetime import datetime
from math import ceil

app = Flask(__name__)

app.secret_key = 'stechtock123'


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('is_admin', False):
            flash('Access denied, admin privileges required!')
            return redirect(url_for('home'))
        return f(*args, **kwargs)

    return decorated_function


@app.route('/')
def home():
    lista_produtos = select(Produto)
    lista_produtos = db_session.execute(lista_produtos).scalars().all()
    result = []
    print(lista_produtos)
    for produto in lista_produtos:
        result.append(produto.serialize())
    return render_template(
        'index.html',
        lista_produtos=result
    )
@app.route('/produtos', methods=['GET', 'POST'])
def produtos():
    return render_template('produtos.html')

@app.route('/produtos/cadastrar', methods=['GET', 'POST'])
def criar_produtos():
    if request.method == 'POST':
        if (not request.form['name'] and not request.form['preco'] and not request.form['descricao'] and not request.form['validade'] and not ['garantia']
        and not ['peso'] and not ['medida'] and not ['id_fornecedor'] and not ['categoria_id']):
            flash('Preencha todos os campos!')
        else:
            novo_produto = Produto(
                nome_produto=str(request.form['name']),
                preco_produto=float(request.form['preco']),
                descricao=str(request.form['descricao']),
                validade_produto=str(request.form['validade']),
                garantia_produto=int(request.form['garantia']),
                peso_produto=float(request.form['peso']),
                medida_produto=str(request.form['medida']),
                id_fornecedor=int(request.form['id_fornecedor']),
                id_categoria_prod=int(request.form['categoria_id']),
            )
            novo_produto.save()
            flash('Produto cadastrado com sucesso!')
            return redirect(url_for('produtos'))
    return render_template('criar_produtos.html')

@app.route('/produtos/listar', methods=['GET', 'POST'])
def listar_produtos():
    # Obtendo o número da página da query string (padrão é 1)
    page = int(request.args.get('page', 1))

    # Defina quantos produtos por página
    per_page = 5

    # Realizando os joins corretamente e limitando os resultados
    lista_produtos = db_session.query(Produto, Categoria, Fornecedor) \
        .join(Categoria, Produto.id_categoria_prod == Categoria.id_categoria_prod) \
        .join(Fornecedor, Produto.id_fornecedor == Fornecedor.id_fornecedor) \
        .limit(per_page) \
        .offset((page - 1) * per_page) \
        .all()

    # Contar o número total de produtos para calcular o número total de páginas
    total_produtos = db_session.query(Produto).count()
    total_pages = ceil(total_produtos / per_page)

    # Passar para o template
    return render_template('consultar_produto.html',
                           lista_produtos=lista_produtos,
                           page=page,
                           total_pages=total_pages)
@app.route('/produtos/editar/<int:id>', methods=['GET', 'POST'])
def editar_produtos(id):
    # Buscar o produto no banco de dados pelo ID
    produto_atualizado = db_session.execute(select(Produto).where(Produto.id_produto == id)).scalar()

    # Se o produto não for encontrado, redirecionar
    if not produto_atualizado:
        flash('Produto não encontrado!')
        return redirect(url_for('produtos'))

    if request.method == 'POST':
        # Verificar se algum campo obrigatório está vazio
        nome = request.form.get('nome')
        preco = request.form.get('preco')
        descricao = request.form.get('descricao')
        validade = request.form.get('validade')
        garantia = request.form.get('garantia')
        peso = request.form.get('peso')
        medida = request.form.get('medida')

        if not nome or not preco or not descricao or not validade or not garantia or not peso or not medida:
            flash('Preencha todos os campos!')
        else:
            # Atualizar os dados do produto
            produto_atualizado.nome_produto = nome
            produto_atualizado.preco_produto = float(preco)  # Convertendo para float
            produto_atualizado.descricao = descricao
            produto_atualizado.validade_produto = validade
            produto_atualizado.garantia_produto = int(garantia)  # Convertendo para int
            produto_atualizado.peso_produto = float(peso)  # Convertendo para float
            produto_atualizado.medida_produto = medida

            # Salvar as alterações no banco
            try:
                db_session.commit()  # Confirmando as alterações no banco de dados
                flash('Modificações salvas com sucesso!')
                return redirect(url_for('produtos'))
            except Exception as e:
                db_session.rollback()  # Reverter em caso de erro
                flash(f'Ocorreu um erro ao salvar as modificações: {e}')

    return render_template('editar_produto.html', produto=produto_atualizado)

@app.route('/produtos/deletar', methods=['GET', 'POST'])
def deletar_produtos():
    if request.method == 'POST':
        # Getting the product ID from the form data
        id = int(request.form['id'])

        # Query the product by its ID
        produto = db_session.query(Produto).get(id)  # Using db_session to query

        if produto:
            try:
                # Delete the product
                produto.delete()  # Using the delete method defined in the Produto class
                db_session.commit()  # Commit the deletion to the database
                return redirect(url_for('listar_produtos'))  # Redirect after deletion
            except Exception as e:
                db_session.rollback()  # Rollback the transaction if there is an error
                return f"Erro ao deletar produto: {e}", 500
        else:
            return "Produto não encontrado", 404  # Return an error if the product is not found

    # Handle GET request: List all products to be displayed in the template
    produtos = db_session.query(Produto).all()
    return render_template("excluir_produto.html", produtos=produtos)


@app.route('/funcionario', methods=['GET', 'POST'])
def funcionarios():
    return render_template('funcionario.html')


@app.route('/funcionario/criar', methods=['GET', 'POST'])
def criar_funcionario():
    if request.method == 'POST':
        # Pegando os dados do formulário
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        telefone = request.form['telefone']
        cargo = request.form['cargo']
        if not nome or not cpf or not email or not telefone or not cargo:
            flash('Preencha todos os campos!')
            return redirect(url_for('criar_funcionario'))        # Criando um novo funcionário
        novo_funcionario = Funcionario(nome_funcionario=nome,
                                        cpf_funcionario=cpf,
                                        email_funcionario=email,
                                        telefone_funcionario=telefone,
                                        cargo_funcionario=cargo,
        )

        # Salvando no banco
        novo_funcionario.save()

        # Redireciona para a página de lista de funcionários ou outra página
        return redirect(url_for('listar_funcionarios'))

    # Exibindo o formulário
    return render_template('criar_funcionario.html')


@app.route('/funcionario/editar', methods=['GET', 'POST'])
def editar_funcionario():
    if request.method == "POST":
        id = int(request.form['id'])

        # Usando db.session para consulta no banco de dados
        funcionario = db_session.query(Funcionario).get(id)

        if funcionario:
            # Atualizando os campos do funcionário com os dados do formulário
            funcionario.nome_funcionario = request.form['nome']  # Corrigido: acessando o campo correto
            funcionario.email_funcionario = request.form['email']
            funcionario.cargo_funcionario = request.form['cargo']
            funcionario.cpf_funcionario = request.form['cpf']
            funcionario.telefone_funcionario = request.form['telefone']

            # Commit para salvar as alterações
            try:
                db_session.commit()
                flash('Funcionário atualizado com sucesso!')
                return redirect(url_for('listar_funcionarios'))  # Redireciona para a lista de funcionários
            except Exception as e:
                db_session.rollback()  # Reverter em caso de erro
                flash(f'Ocorreu um erro ao salvar as modificações: {e}')

        else:
            flash("Funcionário não encontrado!")
            return redirect(url_for('listar_funcionarios'))

    else:
        # Se for GET, recupera o funcionário para preencher o formulário
        id = request.args.get('id')  # Obtém o ID do funcionário a ser editado
        funcionario = db_session.query(Funcionario).get(id)
        if funcionario:
            return render_template("editar_funcionario.html", funcionario=funcionario)
        else:
            flash("Funcionário não encontrado!")
            return redirect(url_for('listar_funcionarios'))


@app.route('/funcionario/lista', methods=['GET'])
def listar_funcionarios():
    page = request.args.get('page', 1, type=int)
    items_per_page = 5

    # Consulta ao banco
    consulta_query = select(Funcionario)
    funcionarios = db_session.execute(consulta_query).scalars().all()

    total_items = len(funcionarios)
    total_pages = (total_items + items_per_page - 1) // items_per_page
    start = (page - 1) * items_per_page
    end = start + items_per_page
    pagination = funcionarios[start:end]

    funcionarios_serializados = [funcionario.serialize() for funcionario in pagination]

    return render_template(
        'consultar_funcionario.html',
        funcionarios=funcionarios_serializados,
        page=page,
        total_pages=total_pages
    )

@app.route('/funcionario/deletar', methods=['GET', 'POST'])
def deletar_funcionario():
    if request.method == 'POST':
        id = int(request.form['id'])
        funcionario = session.query(Funcionario).get(id)
        if funcionario:
            deletar_funcionario(id)
            return redirect(url_for('listar_funcionarios'))
        else:
            return "funcionario não encontrado", 404

        funcionarios=session.query(Funcionario).all()
        return render_template("excluir_funcionario.html", funcionarios=funcionarios)


@app.route('/funcionario/cadastro', methods=['GET', 'POST'])
def cadastro_funcionario():
    if request.method == "POST":
        username = request.form['name']
        cpf = request.form['cpf']
        email = request.form['email']
        telefone = request.form['telefone']
        cargo = request.form['cargo']

        if not username or not cpf or not email or not telefone or not cargo:
            flash('Por favor, preencha todos os campos!')
            return redirect(url_for('cadastro_funcionario'))
        if db_session.query(Funcionario).filter_by(username=username).first():
            flash('Funcionário já existe!')
            return redirect(url_for('cadastro_funcionario'))
        funcionario = Funcionario(name, cpf, email, telefone, cargo)
        db_session.add(funcionario)
        db_session.commit()

        flash('Usuário cadastrado com sucesso!')
        return redirect(url_for('home'))
    return render_template('cadastro_funcionario.html')


@app.route('/fornecedor', methods=['GET', 'POST'])
def fornecedores():
    return render_template('fornecedor.html')


@app.route('/fornecedor/criar', methods=['GET', 'POST'])
def criar_fornecedor():
    if request.method == 'POST':
        # Pegando os dados do formulário
        nome = str(request.form['name'])
        email = str(request.form['email'])
        telefone = str(request.form['tel'])
        if not nome or not email or not telefone:
            flash('Preencha todos os campos!')
            return redirect(url_for('criar_fornecedor'))
        novo_fornecedor = Fornecedor(nome_fornecedor=nome,
                                        email_fornecedor=email,
                                        telefone_fornecedor=telefone,
        )

        # Salvando no banco
        novo_fornecedor.save()

        # Redireciona para a página de lista de funcionários ou outra página
        return redirect(url_for('listar_fornecedor'))

    # Exibindo o formulário
    return render_template('cadastro_fornecedor.html')


@app.route('/fornecedor/editar/<int:id>', methods=['GET', 'POST'])
def editar_fornecedor(id):
    fornecedor_atualizado = db_session.execute(select(Fornecedor).where(Fornecedor.id_fornecedor == id)).scalar()
    if request.method == 'POST':
        if (not request.form['name'] and not request.form['email'] and not request.form['tel']):
            flash('Preencha todos os campos!')
        else:
            fornecedor_atualizado.nome = request.form.get('name')
            fornecedor_atualizado.preco = request.form.get('email')
            fornecedor_atualizado.descricao = request.form.get('tel')
            flash('Modificações salvas com sucesso!')
            return redirect(url_for('fornecedor'))
        fornecedor_atualizado.save()
        return redirect(url_for('listar_fornecedor'))

        # Exibindo o formulário
    return render_template('editar_fornecedor.html')

@app.route('/fornecedor/lista', methods=['GET'])
def listar_fornecedor():
    lista_fornecedores = select(Fornecedor)
    lista_fornecedor = db_session.execute(lista_fornecedores).scalars().all()
    result = []
    print(lista_fornecedor)
    for fornecedor in lista_fornecedor:
        result.append(fornecedor.serialize())
    return render_template('listar_fornecedor.html',
                           fornecedores=result)


@app.route('/fornecedor/deletar', methods=['GET', 'POST'])
def deletar_fornecedor():
    return render_template('excluir_fornecedor.html')


@app.route('/logout')
def logout():
    session.clear()
    flash("Logout efetuado com sucesso!")
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = db_session.query(User).filter_by(username=username).first()
        if not username or not password:
            flash('Preencha todos os campos!')
            return redirect(url_for('login'))
        if user is None:
            flash('Usuário não encontrado!')
            return redirect(url_for('login'))
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = username
            session['is_admin'] = user.is_admin  # Adicione esta linha
            flash('Login realizado com sucesso!')
            return redirect(url_for('home'))
        else:
            flash('Usuário ou senha incorretos!')
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/cadastrousuario', methods=['GET', 'POST'])
def cadastro_usuario():
    if request.method == "POST":
        # Recuperando os valores dos campos do formulário
        username = request.form['username']
        password = request.form['password']
        is_admin = request.form.get('is_admin') == 'on'  # Verifica se o checkbox está marcado

        # Verificando se algum campo está vazio
        if not username or not password:
            flash('Por favor, preencha todos os campos!')
            return redirect(url_for('cadastro_usuario'))  # Redireciona de volta ao formulário

        # Verificando se o usuário já existe
        if db_session.query(User).filter(User.username == username).first():
            flash('Usuário já existe!')
            return redirect(url_for('cadastro_usuario'))  # Redireciona de volta ao formulário

        # Criando o novo usuário
        user = User(username=username, password=password, is_admin=is_admin)  # O hash da senha é gerado no construtor

        # Salvando o novo usuário no banco de dados
        db_session.add(user)
        db_session.commit()

        flash('Usuário cadastrado com sucesso!')
        return redirect(url_for('home'))  # Redireciona para a página inicial

    return render_template('cadastro.html')  # Retorna o formulário de cadastro


@app.route('/registrarproduto', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        if (not request.form['nome'] or not request.form['descricao'] or not request.form['preco'] or not request.form[
            'validade'] or
                not request.form['garantia'] or not request.form['peso'] or not request.form['medida'] or not
                request.form['id'] or
                not request.form['idcatprod']):
            flash('Preencha todos os campos!')
        else:
            cadastro = Produto(
                nome_produto=request.form['nome'],
                descricao=request.form['descricao'],
                preco_produto=float(request.form['preco']),
                validade_produto=request.form['validade'],
                garantia_produto=int(request.form['garantia']),
                peso_produto=float(request.form['peso']),
                medida_produto=float(request.form['medida']),
                id_fornecedor=int(request.form['idfornecedor']),
                id_categoria_prod=int(request.form['idcatprod']),
            )
            print(cadastro)
            cadastro.save()
            db_session.close()
            flash('Cadastro realizado com sucesso!')
            return redirect(url_for('home'))
        return render_template('registro.html')


@app.route('/atividade', methods=['GET', 'POST'])
def atividade():
    if request.method == 'POST':
        movimentacao_tipo = request.form['movimentacao']

        # Verifica se todos os campos obrigatórios estão preenchidos
        if (not request.form['movimentacao'] or not request.form['data'] or not request.form['valor'] or
                not request.form['volume'] or not request.form['id_fun'] or not request.form['id_prod']):
            flash('Preencha todos os campos!')
            return redirect(url_for('atividade'))

        # Define o tipo de movimentação (entrada ou saída)
        entrada = movimentacao_tipo == 'entrada'
        saida = movimentacao_tipo == 'saida'

        if not (entrada or saida):
            flash('Tipo de movimentação inválido!')
            return redirect(url_for('atividade'))

        # Busca pelo funcionário no banco de dados
        funcionario = Funcionario.query.get(request.form['id_fun'])
        if not funcionario:
            flash('Funcionário inválido!')
            return redirect(url_for('atividade'))

        # Busca pelo produto no banco de dados
        produto = Produto.query.get(request.form['id_prod'])
        if not produto:
            flash('Produto inválido!')
            return redirect(url_for('atividade'))

        # Verifica estoque disponível se for uma saída
        if saida and produto.estoque < int(request.form['volume']):
            flash('Estoque insuficiente para a saída!')
            return redirect(url_for('atividade'))

        # Cria a movimentação
        atividade = Movimentacao(
            entrada=entrada,
            saida=saida,
            data_movimento=request.form['data'],
            valor_movimento=request.form['valor'],
            volume_movimento=request.form['volume'],
            id_funcionario=funcionario.id_funcionario,
            id_produto=produto.id_produto,
        )

        # Salva a movimentação
        atividade.save()

        # Atualiza o estoque com base no tipo de movimentação
        if entrada:
            produto.estoque += int(request.form['volume'])  # Aumenta o estoque para entrada
        elif saida:
            produto.estoque -= int(request.form['volume'])  # Reduz o estoque para saída

        # Salva a atualização de estoque
        produto.save()

        db_session.close()
        flash('Atividade realizada com sucesso!')
        return redirect(url_for('home'))

    return render_template('atividade.html')


@app.route('/gerenciamento', methods=['GET', 'POST'])
def gerenciamento():
    return render_template('gerenciamento.html')



@app.route('/relatorio', methods=['GET', 'POST'])
@admin_required
def relatorio():
    # Obter dados de vendas
    movimentacao = db_session.query(Movimentacao).all()

    # Criar o dicionário de dados
    data = {
        'data': [item.data_movimento for item in movimentacao],
        'quantidade': [item.volume_movimento for item in movimentacao],
    }

    # Criar um DataFrame
    df = pd.DataFrame(data)

    # Verificar se o DataFrame está vazio
    if df.empty:
        flash('Nenhum dado disponível para o gráfico.')
        return render_template('relatorio.html', graph=None)

    try:
        # Garantir que as datas estão no formato datetime
        df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d')
    except Exception as e:
        print(f"Erro ao converter datas: {e}")
        flash('Erro ao processar as datas!')
        return render_template('relatorio.html', graph=None)

    # Se o método for POST, filtrar os dados com base nas datas selecionadas
    if request.method == 'POST':
        data_inicio = request.form.get('data_inicio')
        data_fim = request.form.get('data_fim')

        # Verificar se as datas foram fornecidas
        if data_inicio and data_fim:
            try:
                # Converter as datas recebidas do formulário para datetime
                data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
                data_fim = datetime.strptime(data_fim, '%Y-%m-%d')

                # Filtrar os dados dentro do intervalo selecionado
                df = df[(df['data'] >= data_inicio) & (df['data'] <= data_fim)]
            except ValueError:
                flash('Formato de data inválido!')  # Adicione uma mensagem de erro
                pass  # Caso o formato seja inválido, não filtra os dados
        else:
            flash('Por favor, preencha as datas de início e fim.')

    # Verificar novamente se o DataFrame está vazio após o filtro
    if df.empty:
        flash('Nenhum dado disponível para o gráfico após o filtro.')
        return render_template('relatorio.html', graph=None)

    # Criar o gráfico
    fig = px.bar(
        data_frame=df,
        x='data',
        y='quantidade',
        title='Vendas por Data',
        labels={'data': 'Data', 'quantidade': 'Quantidade'},
        color='quantidade',
        color_continuous_scale=px.colors.sequential.Viridis,
        text='quantidade'
    )

    # Atualizar o layout do gráfico
    fig.update_layout(
        title_font=dict(size=24, family='Arial, sans-serif', color='black'),
        xaxis_title='Data',
        yaxis_title='Quantidade',
        xaxis=dict(showgrid=True, gridcolor='LightGray'),
        yaxis=dict(showgrid=True, gridcolor='LightGray'),
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=40, r=40, t=40, b=40)
    )

    # Adicionar rótulos de texto nas barras
    fig.update_traces(texttemplate='%{text}', textposition='outside')

    # Gerar o HTML do gráfico
    graph_html = fig.to_html(full_html=False)

    return render_template('relatorio.html', graph=graph_html, data_inicio=data_inicio, data_fim=data_fim)


if __name__ == '__main__':
    app.run(debug=True)
