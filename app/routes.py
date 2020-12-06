from flask import render_template,url_for,flash,redirect,request
from app import app,db,bcrypt
from app.DB import User,Tracking
from app.forms import LoginForm,RegistrationForm
from flask_login import login_user, current_user, logout_user
from app.Spiders.scrape_spiders import woolsworth,officeWorks



@app.route("/")
@app.route("/home",methods=["GET","POST"])
def home():
    products = ""
    if(current_user.is_authenticated):
        products = Tracking.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html',products=products)

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Tracking.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Tracking Deleted Successfully")
    return redirect(url_for('home'))

@app.route("/tracking",methods=["GET","POST"])
def tracking():
    if(request.method == "POST"):
        url = request.form.get('prod_url')
        set_price = request.form.get('prod_price')
        store = request.form.get('comp_select')
        if(store == "OfficeWorks"):
            product = officeWorks(url)
            price = product['price'].split("$")
            tracking = Tracking(store_name="OfficeWorks",product_url=url,product_name=product['name'],set_price=float(set_price),current_price=float(price[1]),user_id=current_user.id)
        else:
            product = woolsworth(url)
            price = product['price'].split("$")
            print(price)
            tracking = Tracking(store_name="Woolsworth",product_url=url,product_name=product['name'],set_price=float(set_price),current_price=float(price[1]),user_id=current_user.id)
        db.session.add(tracking)
        db.session.commit()
        flash(f'Your can now track your product {product["name"]} in the home page', 'success')
        return redirect(url_for('home'))
    return render_template('tracking.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            USER = current_user.id
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


