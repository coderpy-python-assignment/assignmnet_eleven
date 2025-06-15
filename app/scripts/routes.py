from flask import render_template, redirect, url_for, flash
from app.scripts import app, db
from app.scripts.forms import RegistrationForm
from app.scripts.models import User

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created!', 'success')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)
