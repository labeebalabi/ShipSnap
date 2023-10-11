# from django.shortcuts import render
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,FormView,CreateView,ListView,TemplateView,DetailView
from .forms import*
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.





# Create your views here.
class EHomeView(FormView):
    template_name="home.html"
    form_class=LoginForm
    def post(self,request,*args,**kwrgs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            us = form_data.cleaned_data.get("username")
            pswd = form_data.cleaned_data.get("password")
            user=authenticate(request,username=us,password=pswd)
            if user:
                login(request,user)
                return redirect('h')
            else:
                messages.error(request,"sign in faild")
                return redirect("login")
        return render (request,"home.html",{"form":form_data})
    
class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=User
    success_url=reverse_lazy("login")
