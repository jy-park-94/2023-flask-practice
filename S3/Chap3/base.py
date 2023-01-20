from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)


app.config['SECRET_KEY'] = "asdf"


class SimpleForm(FlaskForm):
    breed = StringField('What breed are you?')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()
    session['breed'] = ''

    if form.validate_on_submit():
        breed_old = session['breed']
        session['breed'] = form.breed.data
        flash(
            f"You\'ve changed your breed from {breed_old} to {session['breed']}!")
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


if __name__ == '__main__':

    app.run(debug=True)
