"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProductForm
from .models import Product

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Always a phone call away.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'So what do we do anyway?',
            'year':datetime.now().year,
        }
    )


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            #redirect to sme admin page
            return redirect('admin_page')
    else:
        form = UserRegisterForm()
    return render(
        request, 
        'app/signup.html', 
        {
            'form':form,
            'title':'Sign up',
            'year':datetime.now().year
            
            })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            #redirect to sme admin page
            return redirect('admin_page')
        else:
            messages.error(request, 'Incorrect username or password')
    return render(request, 'app/login.html', {
        'title':'Log in',
        'year': datetime.now().year
        })


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required(login_url = '/login/')
def admin_page(request):    
    form = ProductForm(request.POST)
    if form.is_valid():
       product = form.save(commit=False)
       product.user = request.user
       product.save()
       return redirect('admin_page')
    else:
       form = ProductForm()
    items = Product.objects.all()
    if (request.GET.get('remove')):
        items.filter(id=request.GET.get('remove')).delete()
        return redirect('admin_page')
    return render(
        request,
        'app/admin_page.html',
        {
        'title':'Administrator',
        'year': datetime.now().year,
        'form':form,
        'items':items
       
       })


@login_required(login_url = '/login/')
def invoicing(request):
    return render(
        request,
        'app/invoicing.html',
        {
        'year': datetime.now().year,
        'title': 'Invoicing'
       })