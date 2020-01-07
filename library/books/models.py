from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=200)


class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()


class Category(models.Model):
    name = models.CharField(max_length=200)


class BookCategory(models.Model):
    #book_id = models.ManyToManyField(Book)
    book_id = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='book_categories')
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='book_categories')


class BookAuthor(models.Model):
    book_id = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='book_authors')
    author_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='book_authors')


class Cart(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='carts')


class CartItem(models.Model):
    cart_id = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='cart_items')
    book_id = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField()
