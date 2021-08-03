"""File for classes"""

class User:
    def __init__(self,email, name, college):
        #email will be used to to distinguish users instead of id
        self.email = email 
        self.name = name
        self.college = college
        
        
class Book:
    def __init__(self, title, author, isbn, price, is_digital):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.is_digital = is_digital
    

        
        