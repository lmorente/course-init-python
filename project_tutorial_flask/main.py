from flask import Flask, redirect, flash, url_for, render_template, request
from datetime import datetime
from flask_mysqldb import MySQL


app = Flask(__name__)

app.secret_key = 'clave'

#connection DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'proyecto_flask'

mysql = MySQL(app)

#Context processors
@app.context_processor
def date_now():
    return {
        'now': datetime.utcnow()
    }

#Endpoints
@app.route('/')
def index():
    age = 18
    return render_template('index.html',
                           data1="Value",
                           data2="NextValue",
                           list=["a", "b"],
                           age=age)

@app.route('/info')
@app.route('/info/<string:name>')
def info(name="Lourdes"):
    return render_template('info.html', name=name)

@app.route('/contact')
@app.route('/contact/<redirection>')
def contact(redirection = None):

    if redirection is not None:
        return redirect(url_for('languages'))

    return render_template('contact.html')

@app.route('/languages')
def languages():
    return render_template('languages.html')

@app.route('/create-car', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':

        brand = request.form['brand']
        model = request.form['model']
        price = request.form['price']
        city = request.form['city']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO coches VALUES(NULL, %s, %s, %s, %s)",
                       (brand, model, price, city))
        cursor.connection.commit()
        flash('Has creado el coche correctamente')
        return redirect(url_for('index'))

    return render_template('create_car.html')



if __name__ == '__main__':
    app.run(debug=True)