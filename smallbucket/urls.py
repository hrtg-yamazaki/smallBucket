from django.urls import path

from smallbucket.views import IndexView, LoginView, LogoutView

app_name = 'smallbucket'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]

