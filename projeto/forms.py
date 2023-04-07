from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField, BooleanField
from wtforms.validators import DataRequired, Length, Email
from flask_wtf.file import FileField, FileAllowed


#lass FormCadastro(FlaskForm):
#   nome = StringField('Nome Completo', validators=[DataRequired()])
#   email = StringField('E-mail', validators=[DataRequired(), Email()])
#   sexo = SelectField('Sexo', choices=['Masculino', 'Feminino', 'Outro'], validators=[DataRequired()])
#   endereco = StringField('Endereço', validators=[DataRequired()])
#   senha = PasswordField('Senha', validators=[DataRequired(), Length(3, 20)])
#   confirmacao = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo(senha)])
#   botao_criar_conta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    nome = StringField('Nome Completo', validators=[DataRequired()])
    sexo = SelectField('Sexo', choices=['Masculino', 'Feminino', 'Outro'], validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    endereco = StringField('Endereço', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(3, 20)])
    botao_submit_login = SubmitField('Fazer Login')
    data_nascimento = DateField('Data de nascimento', validators=[DataRequired()])
    foto = FileField('Insira a sua foto ( PNG, JPG, JPEG )', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
