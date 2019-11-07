from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from .models import User
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from .forms import SignupForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView as AuthLogoutView, LoginView as AuthLoginView
from django.contrib.auth.decorators import login_required

# Create your views here.

class IndexView(TemplateView):

    template_name = "smallbucket/index.html"

index = IndexView.as_view()


class SignupView(CreateView):
    def post(self, request, *args, **kwargs):
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("smallbucket:mypage", pk=request.user.id)
        return render(request, 'smallbucket/signup.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        return  render(request, 'smallbucket/signup.html', {'form': form,})

signup = SignupView.as_view()


class LoginView(AuthLoginView):
    template_name = "smallbucket/login.html"

userlogin = LoginView.as_view()



@login_required
def redirect_view(request):
    return redirect("smallbucket:mypage", pk=request.user.id)




class LogoutView(LoginRequiredMixin, AuthLogoutView):
    template_name = "smallbucket/index.html"

logout = LogoutView.as_view()



class MypageView(LoginRequiredMixin, TemplateView):
    login_url = "/login/"
    template_name = "smallbucket/mypage.html"
    model = User

mypage = MypageView.as_view()


class Identification(UserPassesTestMixin):
    raise_exception = True
    
    def identificate(self):
        user = self.request.user
        return user.pk == self.kwargs["ok"] or user.is_superuser




# class LoginView(TemplateView):
#     def post(self, request, *args, **kwargs):
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             user = User.objects.get(username=username)
#             login(request, user)
#             return redirect("/mypage/")
#         return render(request, "smallbucket/login.html", {"form": form})

#     def get(self, request, *args, **kwargs):
#         form = LoginForm(request.POST)
#         return render(request, "smallbucket/login.html", {"form": form})
