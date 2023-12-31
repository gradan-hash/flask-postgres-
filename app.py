from flask import jsonify
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sendmail import send_mail


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

        if customer == "" or dealer == "" or rating == "" or comments == "":
            return render_template("index.html", message="Please all fields are reqired. Please")

        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:

            data = Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer, rating, comments)

            return render_template('success.html')
        return render_template("index.html", message="You have already submited feedback")


@app.route("/feedback")
def feedback():
    # Fetch all feedback entries from the database
    feedback_data = Feedback.query.all()
    return render_template("feedback.html", feedback_data=feedback_data)


@app.route("/feedback/<int:feedback_id>")
def get_feedback_by_id(feedback_id):
    feedback_entry = Feedback.query.get(feedback_id)
    if feedback_entry:
        # Assuming you have a serialize method
        return jsonify(feedback_entry.serialize())
    return jsonify({"message": "Feedback entry not found"}), 404




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
