"""Utility methods that help with authentication and storage"""
import pyrebase
import urllib.request

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


def login(email, password):
    if email != "" or password != "":
        try:
            auth.sign_in_with_email_and_password(email, password)
            print("Sucessfully signed in!")
        except BaseException:
            print("Invalid user or password. Try again")


def sign_up(email, password):
    if email != "" or password != "":
        try:
            auth.create_user_with_email_and_password(email, password)
            print("Sucess!")
        except BaseException:
            print("Email already exists")


"""STORAGE"""


def upload_file(cloudfileName, fileName):
    if fileName != "":
        storage.child("posts").child(cloudfileName).put(fileName)


def download_file_from_storage(fileName):
    if fileName != "":
        return storage.child("posts").child(
            fileName).download("", "downloaded.txt")


def print_file_from_db(fileName):
    if fileName != "":
        url = storage.child("posts").child(fileName).get_url(None)
        file = urllib.request.urlopen(url).read()
        return file
