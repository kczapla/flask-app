from flask import render_template
from app import app


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
