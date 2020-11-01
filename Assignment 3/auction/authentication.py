from flask import (Blueprint, flash, session, render_template, request, url_for, redirect) 
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from .forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, login_required
from . import db


bp = Blueprint('authentication', __name__, url_prefix='/authentication')

from auction.forms import LoginForm, RegisterForm

@bp.route('/register', methods = ['GET', 'POST']) 
def register(): 
    registerForm = RegisterForm()
    
    if registerForm.validate_on_submit():
            uname =registerForm.user_name.data
            pwd = registerForm.password.data
            email=registerForm.email_id.data
            fname = registerForm.fullname.data
            phnumber = registerForm.phonenumber.data
            add = registerForm.address.data
           
            u = User.query.filter_by(name=uname).first()
            if u:
                flash('User name already exists, please login')
                return redirect(url_for('authentication.login'))
               
            pwd_hash = generate_password_hash(pwd)
            new_user = User(name=uname, password_hash=pwd_hash, emailid=email, fullname = fname, phonenumber = phnumber, address = add)
               
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('main.index'))

    else:
        return render_template('user.html', form=registerForm, heading='Register')
            
    

@bp.route('/logout') 
@login_required
def logout(): 
    logout_user()
    flash('Successfully logged out', 'info')
    return redirect(url_for('authentication.login'))

  


@bp.route('/login', methods=['GET','POST'])
def login():
    loginForm = LoginForm()
    error=None
    if loginForm.validate_on_submit():

        user_name = loginForm.user_name.data
        password = loginForm.password.data
        u = User.query.filter_by(name=user_name).first()
       
        if u is None:
            error='Incorrect user name or password'
       
        elif not check_password_hash(u.password_hash, password): 
            error='Incorrect user name or password'
        if error is None:
            
            login_user(u)
            return redirect(url_for('main.index'))
        else:
            flash(error, 'danger')
    return render_template('user.html', form=loginForm, heading='Login')








    
