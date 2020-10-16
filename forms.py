from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SubmitField, SelectField, StringField
from wtforms import Form
from wtforms.validators import DataRequired, ValidationError, InputRequired

class PolynomialForm(FlaskForm):
    coefficients = StringField(
        label='Coeficientes',
        validators = [
            DataRequired(),
        ],
    )

    down_limit = FloatField(
        label='Limite inferior',
        validators = [
            InputRequired(),
        ],
        default=-1.0,
    )

    upper_limit = FloatField(
        label='Limite superior',
        validators = [
            InputRequired(),
        ],
        default=1.0,
    )

    number_points = SelectField(
        label='Número de pontos',
        validators = [],
        choices=[(50, 50), (100, 100), (250, 250)],
        coerce = int
    )

    def validate_coefficients(self, coefficients):
        pass

    def validate_upper_limit(self, upper_limit):
        if upper_limit.data < self.down_limit.data:
            raise ValidationError("O valor do limite superior não por ser menor que o limite inferior.")
        elif upper_limit.data == self.down_limit.data:
            raise ValidationError("O valor do limite superior não pode ser igual ao valor do limite inferior.")

    def validate_down_limit(self, down_limit):
        if down_limit.data > self.upper_limit.data:
            raise ValidationError("O valor do limite inferior não por ser maior que o limite superior.")
        elif down_limit.data == self.upper_limit.data:
            raise ValidationError("O valor do limite inferior não pode ser igual ao valor do limite superior.")
    