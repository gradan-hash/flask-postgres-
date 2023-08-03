from flask import Flask, request, render_template

app = Flask(__name__)


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
        print(customer, dealer, rating, comments)
        return render_template('success.html')


if __name__ == "__main__":

    app.run(debug=True)
