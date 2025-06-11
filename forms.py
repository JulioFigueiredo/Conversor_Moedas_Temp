from flask_wtf import FlaskForm
from wtforms import SelectField,FloatField, SubmitField
from wtforms.validators import DataRequired

class Temperature(FlaskForm):
    value = FloatField("value", validators=[DataRequired()])
    type = SelectField("Conversion Type", choices=[('c_to_f', 'Celsius->Fahrenheit'),('f_to_c', 'Fahrenheit->Celsius')])
    submit = SubmitField("Convert")