from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')


@app.route('/thank_you')
def thank_you():
    # Get arguments from the HTML form.
    first = request.args.get('first')  # Get argument from the name.
    last = request.args.get('last')
    return render_template('thanks.html', first=first, last=last)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e)


if __name__ == "__main__":
    app.run(debug=True)
