from flask import Flask, render_template, request, abort, redirect
from flask_babel import Babel, gettext
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, DateTimeField
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from flask_datepicker import datepicker
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret'
Bootstrap(app)
datepicker(app)
app.config.update(
DEBUG=True,
#EMAIL SETTINGS
MAIL_SERVER='smtp.googlemail.com',
MAIL_PORT=465,
MAIL_USE_SSL=True,
MAIL_USERNAME = 'sskratoss@gmail.com',
MAIL_PASSWORD = 'ss854184'
)

mail=Mail(app)

def flag_pic(lang):
    if (lang == 'ua'):
        return 'flag-ua'
    elif (lang == 'en'):
        return 'flag-en'
    elif (lang == 'pl'):
        return 'flag-pl'
    return 'flag-ua'


def select_lan(lang):
    if (lang == 'ua'):
        return 'ua'
    elif (lang == 'en'):
        return 'en'
    elif (lang == 'pl'):
        return 'pl'
    return 'ua'


class MyForm(FlaskForm):
    username = StringField("Ім'я та Прізвище:", validators=[InputRequired()])
    email = StringField('Email:', validators=[InputRequired()])
    phone = StringField('Контактний телефон:', validators=[InputRequired()])
    route = SelectField(label='Виберіть маршрут:', validators=[InputRequired()],
                        choices=[('3h', '3 години'), ('4h', '4 години'), ('5h', '5 годин'), ('6h', '6 годин'),
                                 ('7h', '7 годин'), ('8h', '8 годин')])
    empty_textarea = TextAreaField('Ваші побажання:')
    checkbox = BooleanField('Ви погоджуєтеся з умовами бронювання та оплати', validators=[InputRequired()])
    date_time = DateTimeField('Дата і час:', format="%d-%m-%Y   %H:%M", id='datepick', default=datetime.datetime.today() + datetime.timedelta(days = 1), validators=[InputRequired()])




@app.route("/")
def index():
    languages = ['ua', 'en', 'pl']
    print(request.args.get('languages'))
    # lang = request.args.get('languages')
    print(request.form.get('languages'))
    lang = request.args.get('languages')
    flag_name = flag_pic(lang)
    select = select_lan(lang)
    # if request.method == 'POST':
    #     return redirect('index.html', flag_name=flag_name, languages=languages, select=select)
    # flag_name = 'flag-ua'
    return render_template('index.html')


@app.route("/reservation", methods=['GET', 'POST'])
def reservation():
    form = MyForm()
    reserved="2020/03/27,2020/03/28"
    # return render_template('reservation.html', form=form, reserved=reserved)
    if request.method == 'GET':
        return render_template('reservation.html', form=form, reserved=reserved)
    # elif request.method == 'POST':
        # name = request.form.get('username')
        # email = request.form.get('email')
        # print(email)
        # msg = Message(
        #     subject='Hello ' + name,
        #     sender=email,
        #     recipients=
        #     ['email'],
        #     html=render_template("reservation_complete.html"))
        # mail.send(msg)
        # return render_template('reservation_complete.html')
    else:
        return ("ok")


@app.route("/reservation_complete", methods=['GET', 'POST'])
def reservation_complete():
    if request.method == 'GET':
        return render_template('reservation_complete.html')
    elif request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('phone')
        route = request.form.get('route')
        datetimepicker = request.form.get('datetimepicker')
        empty_textarea = request.form.get('empty_textarea')
        print(email)
        msg = Message(
            subject='Прогулянка на яхті для ' + name,
            sender=email,
            recipients=
            [email],
            body=" Ім'я Прізвище: "+ name +",\n Телефон: " + phone + ",\n Маршрут по часу: " + route + ",\n Бажана дата: " + datetimepicker + "\n Коментар:" + empty_textarea,
        )
        mail.send(msg)
        return render_template('reservation_complete.html')

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
        name = request.args.get('name')
    if name:
        return render_template('hello.html', name=name)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
