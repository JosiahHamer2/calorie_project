from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib import messages
#from .filters import fooditemFilter
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib.auth.models import Group
from django.conf import settings

# Create your views here.

#class SignUpView(CreateView):
#	form_class = CustomUserCreationForm
#	success_url = reverse_lazy('login')
#	template_name = 'signup.html'	

def home(request):
	breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()[:5]
	lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()[:5]
	dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()[:5]
	snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()[:5]
	customers = Customer.objects.all()
	context = {'breakfast':breakfast,
			  'lunch':lunch,
			  'dinner':dinner,
			  'snacks':snacks,
			  'customers':customers,
			}
	return render(request,'base.html',context)

def fooditem(request):
	breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()
	bcnt = breakfast.count()
	lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()
	lcnt = lunch.count()
	dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()
	dcnt = dinner.count()
	snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()
	scnt = snacks.count()
	context = {'breakfast':breakfast,
              'bcnt':bcnt,
              'lcnt':lcnt,
              'scnt':scnt,
              'dcnt':dcnt,
              'lunch':lunch,
              'dinner':dinner,
              'snacks':snacks,
            }

	return render(request,'fooditem.html',context)

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is invalid')
    return render(request,'login.html')


def createfooditem(request):
	form = fooditemForm()
	if request.method == 'POST':
		form = fooditemForm(request.POST)
		if form.is_valid():
			form.save()	
			return redirect('/')
	context = {'form':form}
	return render(request, 'createfooditem.html', context)

def addFooditem(request):
	user = request.user
	cust = user.customer
	if request.method == 'POST':
		form = addUserFoodItem(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	form = addUserFoodItem()
	context = {'form':form}
	return render(request, 'addUserFoodItem.html', context)

def userPage(request):
	user = request.user
	cust = user.customer
	fooditems = Fooditem.objects.filter()
	myfilter = fooditemFilter(request.GET, queryset = fooditems)
	fooditems = myfilter.qs
	total = UserFooditem.objects.all()
	myfooditems = total.filter(customer = cust)
	cnt = myfooditems.count()
	querysetFood = []
	for food in myfooditems:
		querysetFood.append(food.fooditem.all())
	finalFoodItems = []
	for items in querysetFood:
		for food_items in items:
			finalFoodItems.append(food_items)
	totalCalories = 0
	for foods in finalFoodItems:
		totalCalories += food.calorie
	CalorieLeft = 2000 - totalCalories
	context={'CalorieLeft':CalorieLeft,'totalCalories':totalCalories,
	'cnt':cnt,'foodlist':finalFoodItems,'fooditem':fooditems,'myfilter':myfilter}
	return render(request,'user.html',context)





