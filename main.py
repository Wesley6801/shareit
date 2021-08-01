import requests
from flask import Flask, render_template, url_for, flash, redirect, request
from util.auth_utils import *
from util.db_utils import *
from classes.classes import *
from booksAPI import *
app = Flask(__name__)
app.config['SECRET_KEY'] = '766ad3b9779f8e26642e74331dbf694c'
STRIPE_API_KEY = 'sk_test_51JIwIkGPV72h4LJb4DzDOGcEvk5egzo5Uu330ulsWD9VCK9oXc9cuoQ1DtTaefvMoiAzJtqKys4uPyEyKxQwu7Bv00vDmhzAoU'


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    unsuccessful = "Make sure the passwords match"
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmed_password = request.form.get('confirmed_password')
        college = request.form.get('college')
        if password == confirmed_password:
            try:
                user = sign_up_user(email, password, name, college)
                return render_template("home.html")
            except BaseException:
                unsuccessful_register = "Something went wrong"
                return render_template(
                    "register.html", unsuccessful=unsuccessful)
        return render_template("register.html", unsuccessful=unsuccessful)
    return render_template("register.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    unsuccessful = "Check your email or password."
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = sign_in_user(email, password)
            return render_template("home.html")
        except BaseException:
            return render_template("login.html", unsuccessful=unsuccessful)

    return render_template("login.html")


@app.route("/searchtest", methods=['GET', 'POST'])
def searchAPI():
    if request.method == "POST":
        print(request.form)
        search = get_bookPrices(
            request.form.get('Bookname'),
            get_bookPrices_json(
                request.form.get('ISBN')))
        ima = get_bookImage(request.form.get('ISBN'))
        if ima == "Error no images for the book.":
            return render_template(
                "search.html",
                text=search[0],
                image=ima,
                test="none",
                text2=ima,
                url=search[1])
        print(ima)
        return render_template(
            "search.html",
            text=search[0],
            image=ima,
            test="block",
            url=search[1])
    return render_template("search.html", test="none")


@app.route("/profile")
def user_profile():
    return render_template("user_profile.html")


@app.route("/share")
def share():
    return render_template("share.html")


"""STRIPE STUFF"""


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/charge', methods=['POST'])
def charge():
    api_key = STRIPE_API_KEY
    token = request.form.get('stripeToken')

    # todo: stripe stuff
    headers = {'Authorization': f'Bearer {api_key}'}
    data = {
        'amount': 22500,
        'currency': 'usd',
        'description': 'Another Charge',
        'source': token
    }

    r = requests.post(
        'https://api.stripe.com/v1/charges',
        headers=headers,
        data=data)

    print(r.text)

    return 'Done'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
