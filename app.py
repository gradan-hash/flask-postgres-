from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'
debug = True

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URL'] = 'postresql://postgres:corne2001nyaa?@localhost/Lambo'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URL'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['radio']
        comments = request.form['comments']

        if customer == "" or dealer == "" or dealer or comments:
            return render_template("index.html", message="Please all fields are reuired. Please")
        print(customer, dealer, rating, comments)
        return render_template('success.html')


if __name__ == "__main__":

    app.run()
