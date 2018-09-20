from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(req):
  context = {
    'users': User.objects.all()
  }
  return render(req, 'users/index.html', context)

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
  try:
    user = User.objects.get(id=user_id)
  except:
    return redirect('/users')

  context = {
    'user': user
  }
  return render(req, 'users/show.html', context)

def edit(req, user_id):
  try:
    user = User.objects.get(id=user_id)
  except:
    return redirect('/users')
  
  context = {
    'user': user
  }
  return render(req, 'users/edit.html', context)

def update(req, user_id):
  valid, response = User.objects.validate_and_update_user(req.POST, user_id)
  if valid == False:
    for error in response:
      messages.error(req, error)
    return redirect('/users/' + user_id + '/edit')

  return redirect('/users')

def delete(req, user_id):
  User.objects.delete_user(user_id)
  return redirect('/users')

def login(req):
  if req.method != 'POST':
    return redirect('/users/new')

  valid, response = User.objects.validate_and_login(req.POST)
  if valid == False:
    for error in response:
      messages.error(req, error)
    return redirect('/users/new')
  else:
    req.session['user_id'] = response.id
    return redirect('/users')