from django.contrib import admin
from .models import *

# Register your models here.

class AuthorModel(admin.ModelAdmin):
    list_display = ['name', 'email','address','date','gender']
admin.site.register(Author,AuthorModel)

class CategoryModel(admin.ModelAdmin):
    list_display = ['name', 'create_at','user']
admin.site.register(Category, CategoryModel)

admin.site.register(Warranty)

class UniteModel(admin.ModelAdmin):
    list_display = ['name', 'create_at','user']
admin.site.register(ItemUnite,UniteModel)


class ItemModel(admin.ModelAdmin):
    list_display = ['name','category','price','item_unite','warranty','user','create_at','update_at']
    search_fields = ['name']
    list_per_page = 15
admin.site.register(Item,ItemModel)



class TransactionModel(admin.ModelAdmin):
    list_display = ['item','quantit','create_at','update_at','user']
admin.site.register(Transaction,TransactionModel)



class StockModel(admin.ModelAdmin):
    list_display = ['item','quantity','create_at','update_at','user']
admin.site.register(Stock,StockModel)
