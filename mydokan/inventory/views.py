from django.shortcuts import render, redirect
from .models import *
from .forms import Transaction_Form, Register_Form
from django.contrib.auth import authenticate, login, logout



# Create Homepage views here.

def home(request):

    item_man = Item.objects.filter(category__id = 5)[:8]
    item_woman = Item.objects.filter(category__id = 6)[:8]
    item_bag = Item.objects.filter(category__id = 7)[:8]
    item_foodware = Item.objects.filter(category__id = 8)[:8]
    category_list = Category.objects.all()

    context = {
        'item_man' : item_man,
        'item_woman' : item_woman,
        'item_bag' : item_bag,
        'item_foodware' : item_foodware,
        'category' : category_list,
    }
    return render(request,'design/index.html',context)



# User REGISTER views
def register_views(request):

    forms = Register_Form(request.POST or None)
    if forms.is_valid():
        instance = forms.save(commit = True)
        instance.save()
        return redirect(login_viwes)

    context = {
        'forms' : forms
    }
    return render(request, 'app/base.html',context)



# Login Views
def login_viwes(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(username = username, password = password)

        if auth is not None:
            login(request, auth)
            return redirect(home)
    return render(request, 'app/base.html')



# Logout Views
def login_viwes(request):

    logout(request)
    return redirect(login_viwes)


# Profile_viwes
def Profile_viwes(request):

    context = {
        'user' : request.user
    }
    return render(request, 'app/base.html',context)


# Create Single page views here.

def single_page_views(request, id):

    single_page = Item.objects.get(id = id)
    related_product = Item.objects.filter(category = single_page.category).exclude(id = id)[:4]
    context = {
        'single_page' : single_page,
        'related_product' : related_product,
    }
    return render(request,'design/single.html',context)



# Create Category views here.
def category_views(request, name):

    cat_filter = Item.objects.filter(category__name = name)
    context = {
        'cat_filter' : cat_filter,
    }
    return render(request, 'design/category.html',context)


# Create Cart Page views here.
def add_cart_views(request, id):

    add_cart = Item.objects.get(id = id)

    # request.session['add_cart'] = True
    session_cart = request.session.get('add_cart', True)

    context = {
        'add_cart' : add_cart,
        'session_cart' : session_cart,
    }
    return render(request, 'design/cart.html',context)


def sales(request):

    if request.method == 'POST':
        form = Transaction_Form(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']

            item_obj = Item.objects.get(name = item_name)
            stk_obj = Stock.objects.get(item = item_obj)
            stk_obj.quantity -= quantity
            stk_obj.save()

            # Transaction.objects.create(
            #     item = item_obj,
            #     quantity = quantity,
            #     status = 'sales'
            # )
            #
            # context = {
            #     'name' : item_name,
            #     'quantity' : quantity
            # }
            # return render(request, 'transaction.html',context)

    form = Transaction_Form()
    context = {
        'form' : form
    }
    return render(request, 'transaction.html',context)
