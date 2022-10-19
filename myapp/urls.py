from django.contrib import admin
from django.urls import path, include
from myapp.views import signup, login, index, contact

urlpatterns = [
    path("", index, name="home"),
    path("signup", signup, name="signup"),
    path("login/", login, name="login"),
    path("contact/", contact, name="contact")
]