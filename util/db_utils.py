import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from classes.classes import *

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def add_user_to_db(user):
    db = firestore.client()
    user_dict = user.__dict__
    db.collection('users').document(user.email).set(user_dict)
    
    
def add_book_to_db(book, owner_email, owner_college):
    db = firestore.client()
    book_dict = book.__dict__
    db.collection('books').document(owner_college).collection(owner_email).document(book.isbn).set(book_dict)
    

