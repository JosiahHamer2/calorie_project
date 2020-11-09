from django.contrib.auth.models import User
from calorie_project.settings import *
from django.db import models

# Create your models here.

class Customer(models.Model):


	user = models.OneToOneField(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200,null=True,unique = True)
	email = models.CharField(max_length=200,null=True)
	date_created = models.DateTimeField(auto_now_add=True,null=True)
	REQUIRED_FIELDS = [user]
	USERNAME_FIELD = 'name'
	is_anonymous = True
	is_authenticated = True
    
	def __str__(self):
		return str(self.name)


class Category(models.Model):

	options = (
		('breakfast', 'breakfast'),
		('lunch', 'lunch'),
		('dinner', 'dinner'),
		('snack', 'snack')
		)

	name = models.CharField(max_length = 50, choices = options)

	def __str__(self):
		return(self.name)



class Fooditem(models.Model):
	name = models.CharField(max_length=200)
	category = models.ManyToManyField(Category)
	calories = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return str(self.name)

class UserFoodItem(models.Model):
	customer = models.ManyToManyField(Customer, blank = True)
	Fooditem = models.ManyToManyField(Fooditem)	