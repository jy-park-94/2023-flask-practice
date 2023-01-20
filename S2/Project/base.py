from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/report')
def report():
    username = request.args.get('username')
    n_reqs = 0
    reqs = [False, False, False]
    for letter in username:
        if letter.isupper():
            reqs[0] = True
            n_reqs += 1
            break
    for letter in username:
        if letter.islower():
            reqs[1] = True
            n_reqs += 1
            break
    if username[-1].isnumeric():
        reqs[2] = True
        n_reqs += 1

    return render_template("report.html", username=username, n_reqs=n_reqs, reqs=reqs)


app.run(debug=True)
