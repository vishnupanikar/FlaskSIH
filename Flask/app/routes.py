from app import server, mongoConn
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, Register
from werkzeug.security import generate_password_hash, check_password_hash
from app.myplot import create_plot

Users = mongoConn.db.users

@server.route('/')
@server.route('/index')
def index():
      return render_template("index.html" , title = 'Home')


@server.route('/login',methods = ['GET','POST'])
def login():
      form = LoginForm()

      if form.validate_on_submit():
            email = form.email.data ; password = form.password.data
            for validate in Users.find({'Email':email}):
                  if validate is not None:
                        if check_password_hash(validate['Password'],password):
                              return redirect(url_for('states'))
                        else:
                              flash('Invalid Password')
                  else:
                        flash('Kindly Register.......')
                        return redirect(url_for('register'))

      return render_template('login.html' , title = 'Login' , form = form)


@server.route('/register' , methods = ['POST','GET'])
def register():
      form = Register()

      if form.validate_on_submit():
            username = form.username.data ; email = form.email.data ; password = form.password.data
            password = generate_password_hash(password)
            userData=None
            for data in Users.find({'Email':email}):
                  userData = data

            if userData is not None:
                  flash('Try different Email')
                  
            else:
                  status = Users.insert_one({'Username':username, 'Email':email, 'Password':password})
                  if status:
                        flash('Registered Successfully....')
                        return redirect(url_for('login'))
            
      return render_template('register.html' , title = 'Register' , form  = form)


@server.route('/states')
def states():
      state = 'MAHARASHTRA'
      fig = create_plot(state)
      return render_template('plot.html' , plot = fig)

@server.route('/change' , methods=['GET','POST'])
def change_state():
      state = request.args['selected']
      fig = create_plot(state)
      return fig
