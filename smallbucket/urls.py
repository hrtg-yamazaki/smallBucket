from django.urls import path
from . import views

app_name = 'smallbucket'
urlpatterns = [
    path('', views.index, name='index'),
    path("signup/", views.signup, name="signup"),
    path("users/<int:pk>/", views.mypage, name="mypage"),
    path("login/", views.userlogin, name="login"),
    path("logout/", views.logout, name="logout"),
    path("redirect/", views.redirect_view, name="redirect")
]

