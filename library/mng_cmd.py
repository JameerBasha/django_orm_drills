from books.models import User, Book, Category, BookCategory, BookAuthor, Cart, CartItem
from random import randrange, choice, randint


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


def add_categories_to_book():
    book_category_list = []
    category = Category.objects.all()
    book_list = Book.objects.all()
    for book in book_list:
        for item_count in range(0, 2):
            book_category_list.append(BookCategory(
                book_id=book, category_id=choice(category)))
    BookCategory.objects.bulk_create(book_category_list)
    return 'Done'


def add_authors_to_book():
    book_author_list = []
    author = User.objects.all()
    book_list = Book.objects.all()
    for book in book_list:
        for item_count in range(0, 1):
            book_author_list.append(BookAuthor(
                book_id=book, author_id=choice(author)))
    BookAuthor.object.bulk_create(book_author_list)
    return 'Done'


def create_carts(start_value, end_value):
    cart_list = []
    users = User.objects.all()
    for value in range(start_value, end_value):
        cart_list.append(Cart(user_id=choice(users)))
    Cart.objects.bulk_create(cart_list)
    return 'Done'


def add_items_to_cart():
    cart_item_list = []
    carts = Cart.objects.all()
    books = Book.objects.all()
    for cart in carts:
        for item_count in range(0, 2):
            cart_item_list.append(
                CartItem(cart_id=cart, book_id=choice(books), quantity=randint(1, 10)))
    CartItem.objects.bulk_create(cart_item_list)
    return 'Done'


def drop_all_tables():
    User.objects.all().delete()
    Book.objects.all().delete()
    Category.objects.all().delete()
    BookCategory.objects.all().delete()
    BookAuthor.objects.all().delete()
    Cart.objects.all().delete()
    CartItem.objects.all().delete()


def create_all_tables():
    create_users(1, 11)
    create_books(1, 41, 10, 100)
    create_categories(1, 11)
    add_categories_to_book()
    add_authors_to_book()
    create_carts(1, 21)
    add_items_to_cart()
