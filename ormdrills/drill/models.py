from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(min=0.0)


class Category(models.Model):
    name = models.CharField(max_length=200)


class BookCategory(models.Model):
    book_id = models.IntegerField()
    category_id = models.CharField(max_length=200)


class BookAuthor(models.Model):
    book_id = models.ForeignKey()
    authod_id = models.IntegerField()


class Cart(models.Model):
    user_id = models.IntegerField()


class CartItem(models.Model):
    cart_id =
    book_id =
    quantity =
