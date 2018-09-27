from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product

# Create your views here.
def index(req):
  if 'user_id' not in req.session:
    return redirect('users:new')
  context = {
    'available_products': Product.objects.exclude(users=req.session['user_id']),
    'cart_products': Product.objects.filter(users=req.session['user_id'])
  }
  return render(req, 'products/index.html', context)

def new(req):
  if 'user_id' not in req.session:
    return redirect('users:new')
  return render(req, 'products/new.html')

def create(req):
  valid, response = Product.objects.validate_and_create_product(req.POST, req.session['user_id'])
  if not valid:
    for error in response:
      messages.error(req, error)
    return redirect('products:new')
  else:
    return redirect('products:index')

def show(req, user_id):
  pass

def edit(req, user_id):
  pass

def update(req, user_id):
  pass

def delete(req, user_id):
  pass

def add_to_cart(req, product_id):
  Product.objects.add_to_cart(product_id, req.session['user_id'])
  return redirect('products:index')

def remove_from_cart(req, product_id):
  Product.objects.remove_from_cart(product_id, req.session['user_id'])
  return redirect('products:index')