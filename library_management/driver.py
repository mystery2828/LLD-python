import sys
sys.path.append('/Users/akash/Desktop/learnings/LLD')

from library_management.services.user_service import UserService
from library_management.controllers.user_controller import UserController
from library_management.services.book_service import BookService
from library_management.controllers.book_controller import BookController
from library_management.services.library_service import LibraryService
from library_management.controllers.library_controller import LibraryController

user_controller = UserController(UserService())
user_controller.addUser(1,"akash")
user_controller.addUser(2,"chethan")
user_controller.addUser(3,"ashwini")

users = user_controller.getUsers()
print(type(users))
for user in users:
    print(users[user].getName())


library_controller = LibraryController(LibraryService())
library_controller.addLibrary(1, "CRP 1")
library_controller.addLibrary(2, "CRP 2")
library_controller.addLibrary(3, "CRP 3")
library_controller.addLibrary(4, "CRP 4")


book_controller = BookController(BookService())
book_controller.addBook(1,"Concept of Physics", 1)
book_controller.addBook(2,"Concept of Maths", 1)
book_controller.addBook(3,"Concept of Biology", 1)
book_controller.addBook(4,"Concept of Chemistry", 1)

books = book_controller.getBooks()
print(type(books))
for book in books:
    print(books[book].getName())