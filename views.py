
from flask import Blueprint, render_template, redirect, request, url_for, flash
import secrets
import os

from flask_login import current_user, login_required, login_user, logout_user
from models import MostSelling, user
import bcrypt


from __init__ import app, db, bcrypt, login_manager

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home/index.html')


@views.route('/about')
def about():
    return render_template('pages/about.html')


@views.route('/contact')
def contact():
    return render_template('pages/contact.html')


@views.route('/food')
def food():
    return render_template('pages/food.html')


@views.route('/reservations',methods=['GET','POST'])
def reservations():
    if request.method == 'POST':

               

                booking = MostSelling(
                    name=request.form['name'], email=request.form['email'],Nooftables=request.form['nooftable'],phone=request.form['phone'])


                db.session.add(booking)

                db.session.commit()

    return render_template('pages/reservations.html')




@views.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    booking=MostSelling.query.all()
    if request.method=='POST':
        if request.form['btn']=='delete' :
            user_delete=MostSelling.query.filter_by(id=request.form['reservation_id']).first()
            
            
            db.session.delete(user_delete)
            
            db.session.commit()
            return redirect(url_for('views.admin'))

        if request.form['btn']=='approve' :
            user_approve=MostSelling.query.filter_by(id=request.form['reservation_id']).first()
            
            
            db.session.delete(user_approve)
            
            db.session.commit()
            return redirect(url_for('views.admin'))
    return render_template('pages/admin.html',booking=booking)






@views.route("/login", methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))


    if request.method == 'POST':

        if request.form['btn'] == 'register':
            print('register')

            if (user.query.filter_by(username=request.form['username']).first()):

                flash("Username is already taken ", "danger")

            elif (user.query.filter_by(email=request.form['email']).first()):

                flash("email is already taken ", "danger")

            else:

                hashed_password = bcrypt.generate_password_hash(
                    request.form['password']).decode('utf-8')

                User = user(
                    username=request.form['username'], email=request.form['email'], password=hashed_password)

                db.session.add(User)

                db.session.commit()


        if request.form['btn'] == 'Login':

            User = user.query.filter_by(
                username=request.form['username_login']).first()

            if User and request.form['password_login']:

                login_user(User)

                next_page = request.args.get('next')

                return redirect(next_page) if next_page else redirect(url_for('views.admin')) ,201

                

    return render_template("pages/login.html", title="login")

@views.route("/Logout")
def Logout():
    logout_user()
    return redirect(url_for("views.home"))
