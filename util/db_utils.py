import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from classes.classes import *

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


def add_user_to_db(user):
    db = firestore.client()
    user_dict = user.__dict__
    print(user_dict)
    db.collection('users').document(user.email).set(user_dict)
    
    
def get_user_from_db(email):
    db = firestore.client()
    result = db.collection('users').document(email).get()
    if result.exists:
        user = from_dict_to_obj(result.to_dict())
        return user
    else:
        return ""

def get_user_by_email(email):
    db = firestore.client()
    users = db.collection('users').where("email", "==", email).get()
    for user in users:
        return user.to_dict()
    
        
def update_user_info(email, value):
    db = firestore.client()
    db.collection('users').document(email).update(value)
    
    
def add_book_to_db(book, owner_college):
    db = firestore.client()
    book_dict = book.__dict__
    db.collection('books').document(owner_college).collection('books').document(book.isbn).set(book_dict)
    
# gets every digital books from the college in the param     
def get_digital_books(college):
    db = firestore.client()
    books = db.collection('books').document(college).collection('books').where("is_paperback", "==", False).get()
    book_list = []
    for book in books:
        book_list.append(book.to_dict())
        print(book.to_dict())
    return book_list

def get_physical_books(college):
    db = firestore.client()
    books = db.collection('books').document(college).collection('books').where("is_paperback", "==", True).get()
    book_list = []
    for book in books:
        book_list.append(book.to_dict())
        print(book.to_dict())
    return book_list
        

def get_paid_books(college):
    db = firestore.client()
    books = db.collection('books').document(college).collection('books').where("price", "!=", "0").get()
    book_list = []
    for book in books:
        book_list.append(book.to_dict())
        print(book.to_dict())
    return book_list
    

def get_userBooks_list(sub, college, email):
    db = firestore.client()
    s = db.collection("books").document(college).collection("books").where("sharer_email","==",email).get()
    f = []
    for v in s:
        f.append(v.to_dict())
    return f

    
# Converts from user dictionary to user object
def from_dict_to_obj(dictionary):
    userObj = User(dictionary.get('email'), 
                  dictionary.get('name'),
                  dictionary.get('college'))
    return userObj