import requests
from flask import (
    Flask,
    render_template,
    url_for,
    flash,
    redirect,
    request,
    session)
from util.auth_utils import *
from util.db_utils import *
from classes.classes import *
from booksAPI import *
from datetime import timedelta
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = '766ad3b9779f8e26642e74331dbf694c'
STRIPE_API_KEY = 'sk_test_51JIwIkGPV72h4LJb4DzDOGcEvk5e' +\
                 'gzo5Uu330ulsWD9VCK9oXc9cuoQ1Dt' +\
                 'TaefvMoiAzJtqKys4uPyEyKxQwu7Bv00vDmhzAoU'
# make sessions last longer - 5 days in this case
app.permanent_session_lifetime = timedelta(days=5)
uploads = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__)),
    'static/uploads')

upload = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__)),
    'static/covers')

pdfs = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__)),
    'static/pdfs')


@app.route("/")
@app.route("/home")
def home():
    if "user" in session:
        # title, author, isbn, price, is_paperback, shared_by, sharer_email,
        # cover_link, pdf_link)
        current_user = session['user']
        current_user_email = current_user.get('email')
        current_user_college = get_user_by_email(
            current_user_email).get('college')
        current_user_token = session.get('user')['idToken']

        digital_section = get_digital_books(current_user_college)
        paperback_section = get_physical_books(current_user_college)
        paid_section = get_paid_books(current_user_college)

        # DIGITAL
        digital_book_list = []
        index = 0
        for book in digital_section:
            #we only want to disply 6 items on main page
            if index <= 6:
                cover_link = get_cover(book.get('isbn'), current_user_token)
                pdf_link = get_pdf(book.get('isbn'), current_user_token)
                title = book.get('title')
                author = book.get('author')
                isbn = book.get('isbn')
                price = book.get('price')
                is_paperback = book.get('is_paperback')
                shared_by = book.get('shared_by')
                sharer_email = book.get('sharer_email')
                bookDisplay = BookDisplay(
                    title,
                    author,
                    isbn,
                    price,
                    is_paperback,
                    shared_by,
                    sharer_email,
                    cover_link,
                    pdf_link)
                digital_book_list.append(bookDisplay)
            index = index+1

        # PAPERBACK
        paperback_list = []
        for book in digital_section:
            if index <= 6:
                cover_link = get_cover(book.get('isbn'), current_user_token)
                pdf_link = get_pdf(book.get('isbn'), current_user_token)
                title = book.get('title')
                author = book.get('author')
                isbn = book.get('isbn')
                price = book.get('price')
                is_paperback = book.get('is_paperback')
                shared_by = book.get('shared_by')
                sharer_email = book.get('sharer_email')
                bookDisplay = BookDisplay(
                    title,
                    author,
                    isbn,
                    price,
                    is_paperback,
                    shared_by,
                    sharer_email,
                    cover_link,
                    pdf_link)
                paperback_list.append(bookDisplay)
            index = index+1

        # PAID
        paid_book_list = []
        for book in paid_section:
            if index <= 6:
                cover_link = get_cover(book.get('isbn'), current_user_token)
                pdf_link = get_pdf(book.get('isbn'), current_user_token)
                title = book.get('title')
                author = book.get('author')
                isbn = book.get('isbn')
                price = book.get('price')
                is_paperback = book.get('is_paperback')
                shared_by = book.get('shared_by')
                sharer_email = book.get('sharer_email')
                bookDisplay = BookDisplay(
                    title,
                    author,
                    isbn,
                    price,
                    is_paperback,
                    shared_by,
                    sharer_email,
                    cover_link,
                    pdf_link)
                paid_book_list.append(bookDisplay)
            index = index+1
        print(len(digital_book_list))
        return render_template(
            "home.html",
            digital_book_list=digital_book_list,
            paperback_list=paperback_list,
            paid_book_list=paid_book_list)
    else:
        return render_template("login.html")


@app.route("/register", methods=['GET', 'POST'])
def register_page():

    if "user" in session:
        return render_template("home.html")

    unsuccessful = "Make sure the passwords match"
    if request.method == "POST":
        session.permanent = True
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmed_password = request.form.get('confirmed_password')
        college = request.form.get('college')
        if password == confirmed_password:
            try:
                user = sign_up_user(email, password, name, college)
                info = auth.get_account_info(user['idToken'])
                email = info['users'][0].get('email')
                # store info in db
                userObj = User(email, name, college)
                add_user_to_db(userObj)
                session['user'] = user
                upload_profile_image(email, "static/uploads/" + "default.png")
                return redirect(url_for("home"))
            except BaseException as err:
                unsuccessful_register = "Something went wrong"
                flash(unsuccessful_register)
                return render_template(
                    "register.html", unsuccessful=unsuccessful)
        flash(unsuccessful)
        return render_template("register.html", unsuccessful=unsuccessful)
    return render_template("register.html")


@app.route("/login", methods=['GET', 'POST'])
def login():

    if "user" in session:
        return render_template("home.html")

    unsuccessful = "Check your email or password."
    if request.method == "POST":
        session.permanent = True
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = sign_in_user(email, password)
            session['user'] = user
            flash("Welcome to ShareIt!")
            return redirect(url_for("home"))
        except BaseException:
            flash(unsuccessful)
            return render_template("login.html", unsuccessful=unsuccessful)
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("token", None)
    return redirect(url_for("login"))


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


@app.route("/profile", methods=['GET', 'POST'])
def user_profile():
    email = session["user"].get('email')
    user = get_user_from_db(email)
    email = user.email
    fullName = user.name
    firstName = fullName.split()[0]
    lastName = ""
    if len(fullName.split()) > 1:
        lastName = fullName.split()[1]
    college = user.college

    if request.method == "POST" and len(request.files) == 0:
        # Updating fields
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        college = request.form.get('college')
        name = firstName + " " + lastName
        update = {
            'email': email,
            'name': name,
            'college': college
        }
        update_user_info(email, update)
        return render_template(
            "user_profile.html",
            fullName=fullName,
            email=email,
            firstName=firstName,
            lastName=lastName,
            college=college,
            pro_image=get_user_profile_url(
                email,
                session['user'].get('idToken')))

    # this should only update the profile-image
    if request.method == "POST" and len(request.files) > 0:
        image = request.files["file"]
        if image:
            image.save(os.path.join(uploads, secure_filename(image.filename)))
            upload_profile_image(
                email,
                "static/uploads/" +
                secure_filename(
                    image.filename))
            return render_template(
                "user_profile.html",
                fullName=fullName,
                email=email,
                firstName=firstName,
                lastName=lastName,
                college=college,
                pro_image=get_user_profile_url(
                    email, session['user'].get('idToken')))
    return render_template(
        "user_profile.html",
        fullName=fullName,
        email=email,
        firstName=firstName,
        lastName=lastName,
        college=college,
        pro_image=get_user_profile_url(email, session['user'].get('idToken')))


@app.route("/share", methods=['GET', 'POST'])
def share():
    if request.method == "POST":
        title = request.form.get('title')
        author = request.form.get('author')
        isbn = request.form.get('isbn')
        is_paper_back = 'is_paper_back' in request.form

        current_user = session['user']
        current_user_email = current_user.get('email')
        current_user_college = get_user_by_email(
            current_user_email).get('college')
        cover = request.files['cover']
        pdf = request.files['pdf']
        shared_by = get_user_by_email(
            current_user_email).get('name')

        price = request.form.get('price')
        book = Book(
            title,
            author,
            isbn,
            price,
            is_paper_back,
            shared_by,
            current_user_email)

        if cover:
            cover.save(os.path.join(upload, secure_filename(cover.filename)))
            upload_book_cover_to_storage(isbn, "static/covers/" +
                                         secure_filename(
                                             cover.filename))
        add_book_to_db(book, current_user_college)

        if request.files['pdf'].filename != "":
            pdf = request.files['pdf']
            if pdf.filename.endswith('.pdf'):
                pdf.save(os.path.join(pdfs, secure_filename(pdf.filename)))
                upload_pdf_to_storage("static/pdfs/" +
                                      secure_filename(
                                          pdf.filename), isbn)

    return render_template("share.html")


@app.route("/mybooks")
def myBooks():
    user = get_user_from_db(session["user"].get('email'))
    ub = get_userBooks_list("books", user.college, user.email)
    if len(ub) == 0:
        flash("You have not shared any books")
        return redirect("/home")
    my_books = []
    for book in ub:
        cover_link = get_cover(book.get('isbn'), session['user'].get('idToken'))
        pdf_link = get_pdf(book.get('isbn'), session['user'].get('idToken'))
        title = book.get('title')
        author = book.get('author')
        isbn = book.get('isbn')
        price = book.get('price')
        is_paperback = book.get('is_paperback')
        shared_by = book.get('shared_by')
        sharer_email = book.get('sharer_email')
        bookDisplay = BookDisplay(
            title,
            author,
            isbn,
            price,
            is_paperback,
            shared_by,
            sharer_email,
            cover_link,
            pdf_link)
        my_books.append(bookDisplay)
    return render_template("mybooks.html", my_books=my_books)

@app.route("/buy")
def buy():
    return render_template("checkout_page.html")


@app.route("/detail")
def detail():
    return render_template("book_details.html")


@app.route("/cart")
def cart():
    return render_template("cart.html")


'''STRIPE STUFF'''


@ app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@ app.route('/charge', methods=['POST', 'GET'])
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
    # todo: create a thank you page
    return 'Done'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
