from flask import Flask, render_template, request, redirect, session, jsonify
from forms import PolynomialForm
from functions import Polynomial, generator_points, str_to_list
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'


@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    form = PolynomialForm()
 
    if request.method == "POST" and form.validate_on_submit():
        session['coefficients'] = form.coefficients.data
        session['down_limit'] = form.down_limit.data
        session['upper_limit'] = form.upper_limit.data
        session['number_points'] = form.number_points.data
        return redirect('result')

    return render_template('index.html', form=form)

@app.route('/result')
def result():
    list_coeffs = str_to_list(session['coefficients'])
    down_limit = session['down_limit']
    upper_limit = session['upper_limit']
    n_points = session['number_points']
    
    linear_space = generator_points(down_limit, upper_limit, n_points)
    polynomial_data = Polynomial(list_coeffs, linear_space)

    data_graph = {
        'x': linear_space.tolist(),
        'y': polynomial_data.tolist()
    }

    return render_template('result.html', data_graph=data_graph)

if __name__ == "__main__":
    app.run(debug=True)