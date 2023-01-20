from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    my_name = "Junyoung"
    letters = list(my_name)
    my_dict = {'pup_name': "Helliful",
               'age': 36,
               'hobby': "biting"}

    return render_template('basic.html', my_name=my_name, letters=letters, my_dict=my_dict)


if __name__ == "__main__":
    app.run(debug=True)
