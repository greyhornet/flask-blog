from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm

import os

app  = Flask(__name__)

app.config['SECRET_KEY'] = '775d4dd5030fa4450e21705f58cbadf2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['FILE_UPLOADS'] = 'C:\\Users\\user\\Desktop\\python\\blog\\Flask_Blog\\static\\files\\uploads'

myposts = [
    {
        'author':'john Doe',
        'title':'first blog',
        'content':'very excited',
        'date_posted':'2020-09-21'
    },
    {
        'author':'Angela Kirby',
        'title':'Climate change',
        'content':'we should counter the green house effect most urgently',
        'date_posted':'2020-04-01'
    },
    {
        'author':'Alan Turing',
        'title':'Enigma',
        'content':'Cracked this bitch',
        'date_posted':'1941-10-28'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=myposts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #validate particular login creds
        if form.email.data == 'pat@innovativetoll.com' and form.password.data == 'erty':
            flash('Login Success', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/upload-file', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':
        if request.files:
            wb = request.files['workbook']
            wb.save(os.path.join(app.config['FILE_UPLOADS'], wb.filename))
            return redirect(request.url)
    return render_template('upload-file.html')

if __name__ == '__main__':
    app.run(debug=True)