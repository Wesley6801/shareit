"""File for classes"""

class User:
    def __init__(self,email, name, college):
        #email will be used to to distinguish users instead of id
        self.email = email 
        self.name = name
        self.college = college
        
        
class Book:
    def __init__(self, title, author, isbn, price, is_paperback, shared_by, sharer_email):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.is_paperback = is_paperback
        self.shared_by = shared_by
        self.sharer_email = sharer_email
        

# This is the class that is going to be shown to the user
class BookDisplay:
     def __init__(self, title, author, isbn, price, is_paperback, shared_by, sharer_email, cover_link, pdf_link):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.is_paperback = is_paperback
        self.shared_by = shared_by
        self.sharer_email = sharer_email
        self.cover_link = cover_link
        self.pdf_link = pdf_link

        
        