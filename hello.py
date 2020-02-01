from flask import Flask, render_template, request, abort, redirect
from flask_babel import Babel, gettext
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
app = Flask(__name__)
app.config['SECRET_KEY']='Thisisasecret'


def flag_pic(lang):
    if(lang=='ua'):
        return 'flag-ua'
    elif(lang=='en'):
        return 'flag-en'
    elif(lang=='pl'):
        return 'flag-pl'
    return 'flag-ua'

def select_lan(lang):
    if(lang=='ua'):
        return 'ua'
    elif(lang=='en'):
        return 'en'
    elif(lang=='pl'):
        return 'pl'
    return 'ua'

class MyForm(FlaskForm):
    username = StringField("Ім'я та Прізвище", validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    phone = StringField('Контактний телефон', validators=[InputRequired()])
    route = SelectField(label='Виберіть маршрут', validators=[InputRequired()], choices=[('3h', '3 години'), ('4h', '4 години'), ('5h', '5 годин'), ('6h', '6 годин'), ('7h', '7 годин'), ('8h', '8 годин')])
    empty_textarea = ""
    full_textarea = ""


@app.route("/")
def index():
    languages = ['ua', 'en', 'pl']
    print(request.args.get('languages'))
    # lang = request.args.get('languages')
    print(request.form.get('languages'))
    lang = request.args.get('languages')
    flag_name=flag_pic(lang)
    select = select_lan(lang)
    # if request.method == 'POST':
    #     return redirect('index.html', flag_name=flag_name, languages=languages, select=select)
    # flag_name = 'flag-ua'
    return render_template('index.html')

@app.route("/reservation")
def reservation():
    form=MyForm()
    return render_template('reservation.html', form=form)


@app.route("/contacts")
def contacts():
    return render_template('contacts.html')

@app.route("/rent_rules")
def rent_rules():
    return render_template('rent_rules.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')



@app.route('/user/<name>')
@app.route('/user/')
def user(name=None):
    if name is None:
        name=request.args.get('name')
    if name:
        return render_template('hello.html', name=name)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)