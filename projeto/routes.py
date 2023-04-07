from flask import render_template, url_for, request, flash, redirect
from projeto import app, database
from projeto.forms import FormLogin
from projeto.models import Usuario


@app.route('/', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario(nome=form_login.nome.data, email=form_login.email.data, senha=form_login.senha.data,
                          sexo=form_login.sexo.data, endereco=form_login.endereco.data,
                          data_nascimento=form_login.data_nascimento.data,
                          foto=form_login.foto.data)

        database.session.add(usuario)
        database.session.commit()

        flash(f'Cadastro feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('login'))
    return render_template('login.html', form_login=form_login)


@app.route('/usuario')
def usuario():
    return render_template('usuario.html')
