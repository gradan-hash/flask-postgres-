from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'
debug = True

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:corne2001nyaa@localhost/Lambo'

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URL'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments


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

        if customer == "" or dealer == "" or dealer == "" or comments:
            return render_template("index.html", message="Please all fields are reuired. Please")
        print(customer, dealer, rating, comments)
        return render_template('success.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
