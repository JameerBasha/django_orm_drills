from books.models import User, Book, Category, BookCategory, BookAuthor, Cart, CartItem
import logging
l = logging.getLogger('django.db.backends')
l.setLevel(logging.DEBUG)
l.addHandler(logging.StreamHandler())


def fetch_book(id):
    return Book.objects.filter(id=id)


def fetch_bulk(id_list):
    return Book.objects.filter(id__in=id_list)


def fetch_book_with_category(category):
    category = Category.objects.get(name=category)
    BookCategory.objects.select_related('book_id').filter(
        category_id=category).all()
