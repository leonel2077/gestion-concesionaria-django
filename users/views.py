from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import (
    authenticate, 
    login, 
    logout,
)
from .forms import UserRegisterForm, UserLoginForm
from rest_framework.authtoken.models import Token

class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )

class LoginView(View):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )
    
    def post(self, request):
        form = self.form_class(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                username=username,
                password=password
            )
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                
                return redirect('index')
        return render(
            request, 
            self.template_name,
            {
                'form': form
            }
        )

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    
