from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(req):
  pass

def new(req):
  return render(req, 'users/new.html')

def create(req):
  if req.method != 'POST':
    return redirect('/users/new')

  valid, response = User.objects.validate_and_create_user(req.POST)
  if valid:
    req.session['user_id'] = response.id
  else:
    for error in response:
      messages.error(req, error)
  return redirect('/users/new')

def show(req, user_id):
  pass

def edit(req, user_id):
  pass

def update(req, user_id):
  pass

def delete(req, user_id):
  pass

def login(req):
  pass