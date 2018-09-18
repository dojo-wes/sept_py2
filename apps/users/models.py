from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
  def validate_and_create_user(self, form):
    errors = []

    if len(form['name']) < 3:
      errors.append('Name must be at least 3 characters long')
    if len(form['username']) < 3:
      errors.append('Name must be at least 3 characters long')
    if not EMAIL_REGEX.match(form['email']):
      errors.append('Email must be valid')
    if len(form['password']) < 8:
      errors.append('Password must be at least 8 characters long')
    if form['password'] != form['confirm']:
      errors.append('Password and confirm must match')

    username_list = self.filter(username=form['username'])
    if len(username_list) > 0:
      errors.append('Username already in use')


    try:
      user = self.get(email=form['email'])
      errors.append("Email already in use")
      return (False, errors)
    except:
      if len(errors) > 0:
        return (False, errors)
      else:
        pw_hash = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
        user = self.create(name=form['name'], username=form['username'], email=form['email'], pw_hash=pw_hash)
        return (True, user)

class User(models.Model):
  name = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  pw_hash = models.CharField(max_length=500)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()

  def __str__(self):
    return self.username