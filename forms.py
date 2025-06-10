from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class Temperatura(FlaskForm):
    temperatura = StringField("tempratura", validators=DataRequired())
    botao_confirmacao = SubmitField("Converter")