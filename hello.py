from flask import Flask, render_template, request, abort, redirect
from flask_babel import Babel, gettext
app = Flask(__name__)


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
    return render_template('reservation.html')


@app.route("/contacts")
def contacts():
    return render_template('contacts.html')

@app.route("/rent_rules")
def rent_rules():
    return render_template('rent_rules.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')


if __name__ == '__main__':
    app.run(debug=True)