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


# user = User("jk@gmail.com", "JK Rownling", "Oxford")
# add_user_to_db(user)

# 978-3-16-148410-0
# title, author, image, isbn
# book = Book("Harry Potter", "JK Rownling", "harry.png", "978-3-16-148410-0")
# add_book_to_db(book, "Emile Conde", "University of New Orleans")

# user = sign_in_user("jack@theman.com", "jack123")
# print(user["idToken"])

# user = sign_up_user("test@gmail.com", 1234567, "test", "somewhere")
# print(user['idToken'])

# try:
#     name = "Joe"
#     college = "Something"
#     user = sign_up_user("test@gmail.com", 1234567, "test", "somewhere")
#     info = auth.get_account_info(user['idToken'])
#     email = info['users'][0].get('email')
#     # store info in db
#     user = User(email, name, college)
#     add_user_to_db(user)
#     # store info in session
#     em = email
#     tk = user['idToken']
#     print(em)
#     print(tk)
# except BaseException as err:
#     print(err)
# print(type(get_user_from_db("jack@theman.com")))
# update_user_info(email="jack@theman.com",value={'email' : 'jack@theman.com', 'name' : 'Jackie', 'college' : 'UNO'})
# print(get_user_by_email("jack@theman.com"))
# update = {
#             'email': 'jack@theman.com',
#             'name': "John",
#             'college': "Princeton"
#         }
# update_user_info("jack@theman.com", update)

# upload_book_to_storage("jack@theman.com", "chillies.png")
# user = sign_in_user("jack@theman.com", "jack123")
# print(user["idToken"])
# print(get_cover_by_isbn("03989894564", user["idToken"]))
# print(type(get_paid_books("CSI")))
# add_to_cart("jack@theman.com", {'email' : 'jack@theman.com', 'name' : 'Jackie', 'college' : 'UNO'})
# print(get_item_from_cart('jack@theman.com'))
# print(get_book_by_isbn('2121121212', 'CSI'))
print(search('Fifi Prindacier', 'CSI'))
