from flask import Flask , request , render_template
import functions, os
app = Flask(__name__)

animal_data = functions.get_the_data('static/animals')

@app.route('/')
def index():
    return render_template('index.html',animal_data=animal_data)


app.route('random_address')
def add():
    return render_template('add.html')


app.route('/login')
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.run()