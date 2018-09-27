from __future__ import unicode_literals

from django.db import models
from ..users.models import User

# Create your models here.
class ProductManager(models.Manager):
  def validate_and_create_product(self, form, user_id):
    errors = []

    if len(form['name']) < 3:
      errors.append('Name must be at least 3 characters long')
    if len(form['description']) < 3:
      errors.append('Description must be at least 3 characters long')
    try:
      price = float(form['price'])
      if price < 0:
        errors.append('Price must be at least $0')
    except:
      errors.append('Price must be a valid number')

    if len(errors) > 0:
      return (False, errors)
    else:
      user = User.objects.get(id=user_id)
      product = self.create(name=form['name'], price=price, description=form['description'], creator=user)
      return (True, product)

  def add_to_cart(self, product_id, user_id):
    try:
      product = self.get(id=product_id)
      user = User.objects.get(id=user_id)
      product.users.add(user)
      product.save()
    except:
      print 'SOMETHING WENT TERRIBLY WRONG'

  def remove_from_cart(self, product_id, user_id):
    try:
      product = self.get(id=product_id)
      user = User.objects.get(id=user_id)
      product.users.remove(user)
      product.save()
    except:
      print 'SOMETHING WENT TERRIBLY WRONG'

class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField()
  description = models.TextField()
  creator = models.ForeignKey(User, related_name="created_products")
  users = models.ManyToManyField(User, related_name="products")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = ProductManager()

  def __str__(self):
    return self.name