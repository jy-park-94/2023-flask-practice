from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return f'''<h1>Let\'s puppify your name!</h1><br><h2>Type your name to localhost:5000/[YOUR_NAME] !</h2>'''


@app.route('/<name>')
def puppify(name):
    newName = None
    if name[-1] != 'y':
        newName = name + "y"
    else:
        newName = name[:-1] + "iful"
    return f'<h1> Hello, {newName}! </h1>'


if __name__ == '__main__':
    app.run(debug=True)
