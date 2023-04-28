from django.urls import path
from . import views

urlpatterns = [
    path("HomePage", views.HomePage, name="HomePage"),
    path("register", views.register, name="register"),
    path("", views.LoginPage, name="LoginPage"),
    path("logoutPage", views.logoutPage, name="logoutPage"),
]
