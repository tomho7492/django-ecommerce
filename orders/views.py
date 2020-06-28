from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import CartItem, Pizza, Order
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {"user": request.user,
               "pizzas": Pizza.objects.all()
               }


    return render(request, "orders/index.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials"})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def register_view(request):
    if request.method == 'GET':
        return render(request, "orders/register.html")
    username = request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    user = User.objects.create_user(username, email, password)
    user.save()
    return HttpResponseRedirect(reverse("index"))

def cart(request):
    user = request.user

    if request.method == 'POST':
        pizzapk = request.POST["pizzapk"]
        pizza = Pizza.objects.get(pk=pizzapk)
        if CartItem.objects.filter(User=user, pizzas=pizza).count() > 0:
            cartItem = CartItem.objects.get(User=user, pizzas=pizza)
            cartItem.Quantity += 1
            cartItem.save()
            print("quantity" + str(cartItem.Quantity))
        else:
            CartItem.objects.create(pizzas=pizza, User=user, Cost=pizza.cost)

    query = CartItem.objects.filter(User=user)
    totalCost = 0
    for cartItem in query:
        cartItem.Cost = cartItem.pizzas.cost * cartItem.Quantity
        cartItem.Cost = round(cartItem.Cost, 2)
        cartItem.save()
        totalCost += cartItem.Cost

    query = CartItem.objects.filter(User=user)
    totalCost = round(totalCost, 2)
    context= {"pizzas": query, "totalCost":totalCost}
    return render(request, "orders/cart.html", context)

def removeFromCart(request):
    user = request.user
    cartItemID = request.POST["cartItem"]
    intTemp = int(cartItemID)
    temp = CartItem.objects.filter(User=user, id=intTemp)
    temp.all().delete()
    return  HttpResponseRedirect('/cart')

def checkout(request):

    user = request.user

   #Order.objects.filter(User=user).all().delete()
    #print("deleted")

    items = CartItem.objects.filter(User=user)
    string = ""
    for item in items:
      string += str(item) + ", "
    totalCost = 0
    for cartItem in items:
        totalCost += cartItem.pizzas.cost * cartItem.Quantity
    totalCost = round(totalCost, 2)
    if items.count() > 0:
        Order.objects.create(User=user, items=string, totalCost=totalCost)
        CartItem.objects.filter(User=user).all().delete()
    else:
        return  HttpResponseRedirect('/')
    orders = Order.objects.filter(User=user)
    context = {"Orders":orders, "totalCost":totalCost}
    return render(request, "orders/checkout.html", context)

def orders(request, id):
    user = request.user
    if Order.objects.filter(User=user, id=id).count() < 1:
        return  HttpResponseRedirect('/')
    order = Order.objects.get(User=user, id=id)
    print(str(order))
    context = {"Order":order}
    return render(request, "orders/order.html", context)