"""File for classes"""

class User:
    def __init__(self,email, name, college):
        #email will be used to to distinguish users instead of id
        self.email = email 
        self.name = name
        self.college = college
        
        
class Book:
    def __init__(self, title, author, image, isbn):
        self.title = title
        self.author = author
        self.image = image
        self.isbn = isbn
    

        
        