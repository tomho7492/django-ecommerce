from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("cart", views.cart, name="cart"),
    path("removeFromCart", views.removeFromCart, name="removeFromCart"),
    path("checkout", views.checkout, name="checkout"),
    path("orders/<int:id>", views.orders, name="orders")
]
