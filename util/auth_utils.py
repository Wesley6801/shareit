"""Utility methods that help with authentication and storage"""
import pyrebase
import urllib.request
from classes.classes import *
from util.db_utils import *
import os.path

# Pyrebase setup
firebaseConfig = {
    'apiKey': "AIzaSyBbrX_lY0Jr-pZe551OzcDWbWj81A-cEUw",
    'authDomain': "shareit-c7665.firebaseapp.com",
    'projectId': "shareit-c7665",
    'storageBucket': "shareit-c7665.appspot.com",
    'messagingSenderId': "630842739993",
    'appId': "1:630842739993:web:be17150dadaccfee2ac988",
    'measurementId': "G-NM6R9QPEMX",
    'databaseURL': ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
storage = firebase.storage()


def sign_in_user(email, password):
    user = auth.sign_in_with_email_and_password(email, password)
    print("Sucessfully signed in!")
    return user


def sign_up_user(email, password, name, college):
    user = auth.create_user_with_email_and_password(email, password)
    print("Sucess!")
    return user


def get_user_acc_info(user_id_token):
    return auth.get_account_info(user_id_token)


"""STORAGE"""


def upload_profile_image(email, fileName):
    if fileName != "":
        storage.child("user_profile_imgs").child(
            email).child("profile.png").put(fileName)


def download_user_profile(email, fileName):
    if fileName != "":
        try:
            return storage.child("user_profile_imgs").child(
                email).child("profile.png").download("", fileName + "s")
        except:
            return ""
    return ""


# Needs user profile token
def get_user_profile_url(email, user_id_token):
    url = storage.child("user_profile_imgs").child(
        email).child("profile.png").get_url(user_id_token)
    return url



def upload_book_cover_to_storage(email, isbn, book):
    if isinstance(book, str):
        try:
            storage.child("images").child(email).child(isbn).put(book)
            return True
        except BaseException:
            return False
    return False


def upload_pdf_to_storage(email,file, isbn):
     storage.child("pdfs").child(email).child(isbn).put(file)


def get_book_from_storage(email, book):
    b = isinstance(book, str)
    e = isinstance(email, str)
    if b and e:
        try:
            return storage.child("images").child(email).child(
                email).download("", book + "s")
        except BaseException:
            return ""
    return ""
