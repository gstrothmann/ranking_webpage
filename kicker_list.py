from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from get_data import get_data
import json, plotly

app = Flask(__name__)

app.config['SECRET_KEY'] = '0798aaa973a4f300d8a2277a9db963f2'

passed_data = get_data()


@app.route('/')
@app.route('/home')
def home():
    name = request.args.get("name", "World")
    return render_template('home.html', data = passed_data)

@app.route('/about')
def about():
    return render_template('about.html', data = passed_data)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@kicker-list.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessfull. Please check username and password.', 'danger')
    return render_template('login.html', title = 'Login', form = form)

if __name__ == '__main__':
    app.run(debug = True)