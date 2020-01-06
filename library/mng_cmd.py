from books.models import User, Book, Category, BookCategory, BookAuthor, Cart, CartItem
from random import randrange


def create_users(start_value, end_value):
    user_list = []
    for value in range(start_value, end_value):
        user_list.append(User(user_name='u'+str(value)))
    User.objects.bulk_create(user_list)
    return 'Done'


def create_books(start_value, end_value, start_price, end_price):
    book_list = []
    for value in range(start_value, end_value):
        book_list.append(
            Book(title='b'+str(value), price=randrange(start_price, end_price)))
    Book.objects.bulk_create(book_list)
    return 'Done'


def create_categories(start_value, end_value):
    category_list = []
    for value in range(start_value, end_value):
        category_list.append(Category(name='c'+str(value)))
    Category.objects.bulk_create(category_list)
    return 'Done'


def add_categories_to_book(category_start_id, category_end_id):
    book_category_list = []
    books = Book.objects.value(id).all()
    print(books)
