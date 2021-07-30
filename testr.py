"""This is just a class to test features. It's not part of the project"""
from util.auth_utils import *
from util.db_utils import *
from classes.classes import *

# email = input("Enter your email ")
# password = input("Enter your password ")
# sign_up(email, password)

# upload_file("lorem", "dummy.txt")

# download_file_from_storage("lorem")

# test()
# upload_profile_image("20930sfo23w", "chillies.png")
# download_user_profile("20930sfo23w", "chillies.png")
# email = 'jack@theman.com'
# password = 'jack123'
# user = login(email, password)


# info = get_user_acc_info(user['idToken'])
# print(info['users'][0].get('email'))
# url = get_user_profile_url(user['idToken'])
# print(url)


# user = sign_up("somebody@hotmail.com", "1234567")
# info = get_user_acc_info(user['idToken'])
# print(info['users'][0].get('email'))


# sign_up_user("jm@gmail.com", "1234567", "John Macabre", "Sentinel")


user = User("jk@gmail.com", "JK Rownling", "Oxford")
add_user_to_db(user)

# 978-3-16-148410-0
# title, author, image, isbn
book = Book("Harry Potter", "JK Rownling", "harry.png", "978-3-16-148410-0")
add_book_to_db(book, "Emile Conde", "University of New Orleans")
