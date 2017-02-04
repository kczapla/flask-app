from flask import flash, redirect, render_template
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day'
        },
        {
            'author': {'nickname': 'Susane'},
            'body': 'Wonderful'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           posts=posts,
                           user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           providers=app.config['OPENID_PROVIDERS'],
                           form=form)
