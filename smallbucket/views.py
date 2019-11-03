from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView

# Create your views here.

class IndexView(TemplateView):

    template_name = "smallbucket/index.html"


class LoginView(AuthLoginView):

    template_name = "smallbucket/login.html"


class LogoutView(AuthLogoutView):

    template_name = "smallbucket/index.html"