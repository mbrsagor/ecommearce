from django.db import models
from django.contrib.auth.models import User


# Create User models here.
class Author(models.Model):
    name = models.ForeignKey(User, on_delete = models.CASCADE)
    email = models.EmailField(max_length = 45)
    address = models.CharField(max_length = 50)
    date = models.DateTimeField(auto_now_add = True, auto_now = False)
    GENDER_CHOOSE = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(choices = GENDER_CHOOSE, max_length = 8)

    def __str__(self):
        return self.name.username



class Category(models.Model):
    name = models.CharField(max_length = 70, unique =  True)
    create_at = models.DateTimeField(auto_now = True, auto_now_add = False)
    image = models.ImageField(upload_to = 'category_images', blank = True, null = True)
    user = models.ForeignKey(Author, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class Warranty(models.Model):
    name = models.CharField(max_length = 80, unique =  True, null = True, blank = True)
    create_at = models.DateTimeField(auto_now = True, auto_now_add = False)
    user = models.ForeignKey(Author, on_delete = models.CASCADE)

    def __str__(self):
        return self.name



class ItemUnite(models.Model):
    name = models.CharField(max_length = 50, unique =  True)
    create_at = models.DateTimeField(auto_now = True, auto_now_add = False)
    user = models.ForeignKey(Author, on_delete = models.CASCADE)

    def __str__(self):
        return self.name




class Item(models.Model):
    name = models.CharField(max_length = 100, unique =  True)
    description = models.TextField()
    price = models.IntegerField()
    regular_price = models.IntegerField()
    discount_price = models.IntegerField()
    image = models.ImageField(upload_to = 'item')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    item_unite = models.ForeignKey(ItemUnite, on_delete = models.CASCADE)
    warranty = models.ForeignKey(Warranty, on_delete = models.CASCADE)
    user = models.ForeignKey(Author, on_delete = models.CASCADE)
    create_at = models.DateTimeField(auto_now = True, auto_now_add = False)
    update_at = models.TimeField(auto_now = True, auto_now_add = False)



    def __str__(self):

        return self.name


class Stock(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    create_at = models.DateTimeField(auto_now = True, auto_now_add = False)
    update_at = models.TimeField(auto_now = True, auto_now_add = False)
    user = models.ForeignKey(Author, on_delete = models.CASCADE)


    def __str__(self):
        return self.item.name


class Transaction(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    quantit = models.IntegerField()
    create_at = models.DateTimeField(auto_now = True, auto_now_add = False)
    update_at = models.TimeField(auto_now = True, auto_now_add = False)
    user = models.ForeignKey(Author, on_delete = models.CASCADE)
    STATUS_CHOOSE = (
        ('buy', 'Buy'),
        ('sales', 'Sales'),
    )
    status = models.CharField(choices = STATUS_CHOOSE, max_length = 6)

    def __str__(self):
        return self.item.name
